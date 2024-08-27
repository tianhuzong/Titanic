import paddle
import loguru
import tqdm
import numpy as np

def train(model, max_epoch, lossfn, train_loader, test_loader):
    
    lr_scheduler = paddle.optimizer.lr.ReduceOnPlateau(0.0005, factor=0.85, patience=100, verbose = True)
    opt = paddle.optimizer.Adam(learning_rate=lr_scheduler, parameters=model.parameters())
    with tqdm.tqdm(total=max_epoch,desc="training",unit="epoch") as pbar:
        loguru.logger.info("开始训练")
        losses = []
        for epoch in range(max_epoch):
            model.train()
            epoch_loss = []
            for id, (x, y) in enumerate(train_loader):
                output = model(x)
                loss = lossfn(output, y)

                loss.backward()
                opt.step()
                opt.clear_grad()
                
                epoch_loss.append(loss.detach())  # detach() 可以防止反向传播
                

            # 计算平均损失
            loss_ = paddle.mean(paddle.stack(epoch_loss)).item()  
            right_num = test(model, lossfn, test_loader)
            test_on_traindata(model, lossfn, train_loader)
            lr_scheduler.step(right_num)
            losses.append({"epoch": epoch + 1,"loss": loss_, "acc": right_num})
            loguru.logger.info(f"epoch {epoch + 1}, loss: {loss_}, acc: {right_num}")
            if (epoch + 1) % 10 == 0:
                paddle.save(model.state_dict(), "./checkpoints/model_epoch_" + str(epoch + 1) + ".pdparams")
            loguru.logger.info(f"model saved at epoch {epoch + 1}")
            pbar.update(1)
                
    paddle.save(opt.state_dict(), "./checkpoints/opt_epoch_" + str(max_epoch) + ".pdopt")
    loguru.logger.info(f"训练完成")
    #loguru.logger.info(f"{opt.state_dict()}")
    a = max(losses, key=lambda x:x["acc"])
    loguru.logger.info(f"最佳选项: {a}")
    
    return losses
        

def test(model, lossfn, test_loader, dataname="测试"):
    model.eval()
    right_num = 0
    total_num = 0

    for batch_id, data in enumerate(test_loader()):
        x_data = data[0]  # 测试数据
        y_data = data[1]  # 测试标签
        predicts = model(x_data)  # 预测结果

        # 计算损失与精度
        loss = lossfn(predicts, y_data)
        
        # 逐元素比较
        predicted_labels = predicts.argmax(axis=1)
        true_labels = y_data.astype("int64")

        right_num += (predicted_labels == true_labels).sum().numpy()
        total_num += true_labels.shape[0]  # 统计总样本数

    # 打印准确率
    accuracy = right_num / total_num
    loguru.logger.info(f"{dataname}集准确率为：{accuracy}")
    return accuracy

def test_on_traindata(model, lossfn, train_loader):
    test(model, lossfn, train_loader, "训练")

