import {ElMessage} from "element-plus";
var fetchDatares;
function fetchData(url, input_data) {
    // 解析 JSON 字符串
    // 发起 POST 请求
    
    $.ajax(
        {
            url:url,
            type:"POST",
            data:JSON.stringify(input_data),
            dataType:"json",
            contentType: "application/json",
            async:false,
            success:function(response){
                fetchDatares = response;
                console.log(response);
            }
        }
    );
    return fetchDatares;
}


export  function predict(
    sex, // 男1 女0
    age, // 年龄
    fare, // 票价
    embarked, // 登船港口 C=1 Q=2 S=3
    ticketClass, // 船票类别 1 2 3
    name, // 身份 Master Miss Mr Mrs Officer Royalty
    cabin, // 船舱号 A-T and U
    familySize // 家庭人数 包含自己
){
    var are_they_definded = [
        sex, age, fare, embarked, ticketClass, name, cabin, familySize
    ].every(r => r !== undefined && r !== null && r !== '');
    if (!are_they_definded){
        ElMessage({message : "请填写所有必填项", type: "error"});
        return null;
    }
    var data = {
        sex: sex,
        age: age,
        fare: fare,
        embarked: embarked,
        ticket_class: ticketClass,
        name: name,
        cabin: cabin,
        family_size: familySize
    };
    const url = "https://ojvfxv-nkecab-8000.preview.cloudstudio.work/predict";
    var value = null;
    ElMessage("已发起请求,请等待");
    value =  fetchData(url, data);
    if (value == null){
        ElMessage({message : "请求失败,请前往服务端查看", type: "error"});
        return null;
    }
    return value;
}
