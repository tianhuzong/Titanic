import * as ort from 'onnxruntime-web';

export function create_session(model_path) {
    return ort.InferenceSession.create(model_path);
}

export function buildTensor(
    sex, // 男1 女0
    age, // 年龄
    fare, // 票价
    embarked, // 登船港口 C=1 Q=2 S=3
    ticketClass, // 船票类别 1 2 3
    name, // 身份 Master Miss Mr Mrs Officer Royalty
    cabin, // 船舱号 A-T and U
    familySize // 家庭人数 包含自己
) {
    let targetList = [];
    targetList.push(sex);
    targetList.push(age);
    targetList.push(fare);

    let temp = [0, 0, 0];
    temp[embarked - 1] = 1;
    targetList.push(...temp);

    temp = [0, 0, 0];
    temp[ticketClass - 1] = 1;
    targetList.push(...temp);

    const nameCategories = "Master Miss Mr Mrs Officer Royalty".split(" ");
    let t2 = [0, 0, 0, 0, 0, 0];
    t2[nameCategories.indexOf(name)] = 1;
    targetList.push(...t2);

    const cabinCategories = "A B C D E F G T U".split(" ");
    t2 = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    t2[cabinCategories.indexOf(cabin)] = 1;
    targetList.push(...t2);

    targetList.push(familySize);

    temp = [0, 0, 0];
    temp[0] = familySize === 1 ? 1 : 0;
    temp[1] = familySize >= 2 && familySize <= 4 ? 1 : 0;
    temp[2] = familySize > 4 ? 1 : 0;
    targetList.push(...temp);

    const inputTensor = new ort.Tensor('float32', new Float32Array(targetList), [targetList.length,]);
    return targetList;
}


export async  function predict(session, inputTensor) {
    const feeds = { input: inputTensor };
    const results = await session.run(feeds);
    return results.output.data;
}