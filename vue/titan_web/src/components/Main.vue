<template>
    <el-form :inline="true" :model="form" label-width="auto" style="max-width: 1200px">
        <el-form-item label="Age(年龄):">
            <el-input-number v-model="age" :min=0  placeholder="Please input" style="width: 240px" />
        </el-form-item>
        <el-form-item label="Fare(票价):">
            <el-input-number v-model="fare" :min=0  placeholder="Please input" style="width: 240px" />
        </el-form-item>
        <el-form-item label="Family Size(家庭人数):">
            <el-input-number v-model="family_size" :min=1  placeholder="Please input" style="width: 240px" />
        </el-form-item>
        <el-form-item label="Sex(性别):">
            <el-select
                v-model="sex"
                placeholder="Select"
                size="large"
                style="width: 240px"
                >
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </el-form-item>
        <el-form-item label="Cabin class(客舱等级):">
            <el-select
                v-model="ticket_class"
                placeholder="Select"
                size="large"
                style="width: 240px"
                >
                <el-option
                    v-for="item in ticket_classes"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </el-form-item>
        <el-form-item label="Title(头衔):">
            <el-select
                v-model="name_title"
                placeholder="Select"
                size="large"
                style="width: 240px"
                >
                <el-option
                    v-for="item in titles"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </el-form-item>
        <el-form-item label="Cabin(客舱号):">
            <el-select
                v-model="cabin"
                placeholder="Select"
                size="large"
                style="width: 240px"
                >
                <el-option
                    v-for="item in cabins"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </el-form-item>
        <el-form-item label="Embarked(登船港口):">
            <el-select
                v-model="embarked"
                placeholder="Select"
                size="large"
                style="width: 400px"
                >
                <el-option
                    v-for="item in embarkeds"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button @click="on_submit" id="submit_button" :disabled="submit_button_disable" size="large">提交(submit)</el-button>
            <el-button @click="on_clear_value" id="clear_button" size="large">清空(clear)</el-button>
            <el-button @click="default_value" id="default_button" size="large">默认值(default)</el-button>
        </el-form-item>
    </el-form>
    
</template>

<script setup>
import { ref } from 'vue';
import * as titanUtil from "../utils";
import { ElMessage, ElMessageBox } from 'element-plus'
import VideoPlayer from "./VideoPlayer.vue";
import {useVideoPlayer} from "../useVideoPlayer.js"



const options = [
    {
        value: 1,
        label: 'Male(男)'
    },
    {
        value: 0,
        label: 'Female(女)'
    }
];

const embarkeds = [
    {
        value: 1,
        label: 'Cherbourg-Octeville,Frence 瑟堡-奥克特维尔[法国]'
    },
    {
        value: 2,
        label: 'Queenstown,Ireland 昆士敦[爱尔兰]'
    },
    {
        value: 3,
        label: 'Southampton,England 南安普敦[英国]'
    }
];

const ticket_classes = [
    {
        value: 1,
        label: '1st(一等舱)'
    },
    {
        value: 2,
        label: '2nd(二等舱)'
    },
    {
        value: 3,
        label: '3rd(三等舱)'
    }
];

const titles = [
    {
        value: "Mr",
        label: 'Mr(先生)'
    },
    {
        value: "Mrs",
        label: 'Mrs(夫人)'
    },
    {
        value: "Miss",
        label: 'Miss(小姐)'
    },
    {
        value: "Master",
        label: 'Master(有技能的人/教师)'
    },
    {
        value: "Officer",
        label: 'Officer(军官)'
    },
    {
        value: "Royalty",
        label: 'Royalty(皇室成员)'
    }

];

const cabins = [
    {
        value: "A",
        label: 'A'
    },
    {
        value: "B",
        label: 'B'
    },
    {
        value: "C",
        label: 'C'
    },
    {
        value: "D",
        label: 'D'
    },
    {
        value: "E",
        label: 'E'
    },
    {
        value: "F",
        label: 'F'
    },
    {
        value: "G",
        label: 'G'
    },
    {
        value: "T",
        label: 'T'
    },
    {
        value: "U",
        label: 'Unknown'
    }
];

const sex =  ref();
const age =  ref();
const fare = ref(); 
const embarked = ref(); 
const ticket_class = ref(); 
const name_title = ref(); 
const cabin = ref(); 
const family_size = ref(); 
const submit_button_disable = ref(false);

/*
const sex = ref(1);
const age = ref(11);
const fare = ref(7.5);
const embarked = ref(1);
const ticket_class = ref(1);
const name_title = ref("Officer");
const cabin = ref("A");
const family_size = ref(11);
const submit_button_disable = ref(false);

*/

var {canvas, play} = useVideoPlayer();
//console.log(canvas.value);
$(document).ready(function (){
    let {canvas, play} = useVideoPlayer();
    console.log("canvas.value:",canvas.value);
    play();
});

const on_submit = () => {
    submit_button_disable.value = true;
    console.log("input_value:",sex.value, age.value, fare.value, embarked.value, ticket_class.value, name_title.value, cabin.value, family_size.value);
    var output_data = null;
    output_data = titanUtil.predict(sex.value, age.value, fare.value, embarked.value, ticket_class.value, name_title.value, cabin.value, family_size.value);
    //output_data = output_data !== undefined ?  output_data.resul : titanUtil.predict(sex.value, age.value, fare.value, embarked.value, ticket_class.value, name_title.value, cabin.value, family_size.value);
    
    setTimeout(() => {
        console.log("等待1s给他请求")
        /*
        ElMessageBox.alert(output_data.result ? "可以存活" : "无法存活", '预测结果', {
            // if you want to disable its autofocus
            // autofocus: false,
            confirmButtonText: 'OK',
        });
        */
        console.log("canvas.value:",window.canvas.value);
        try{
            play(() => {
                submit_button_disable.value = false;
            }, output_data.result ? "/alive.mp4" : "/dead.mp4");
        }catch(e){
            submit_button_disable.value = false;
            if (output_data !== null){
                ElMessage({message:"发生错误,错误信息"+e, type:"error" });
            }
        }
    }, 1000);
}

const on_clear_value = () => {
    sex.value = undefined;
    age.value = undefined;
    fare.value = undefined;
    embarked.value = undefined;
    ticket_class.value = undefined;
    name_title.value = undefined;
    cabin.value = undefined;
    family_size.value = undefined;

}

function all_not_undefind() {
  // 检查每个 ref 的 value 是否存在且不为空
  return [
    sex, age, fare, embarked, ticket_class, name_title, cabin, family_size
  ].every(r => r.value !== undefined && r.value !== null && r.value !== '');
}

function default_value() {
    // 为每个 ref 的 value 赋默认值
    sex.value = 1;
    age.value = 11;
    fare.value = 7.5;
    embarked.value = 1;
    ticket_class.value = 1;
    name_title.value = "Officer";
    cabin.value = "A";
    family_size.value = 11;

}

</script>