<script setup>
import { ref, watch } from 'vue'
import * as titanUtil from "../utils"
import Main from "./Main.vue"
import {useVideoPlayer} from "../useVideoPlayer.js";
import VideoPlayer from "./VideoPlayer.vue";

const {canvas, play} = useVideoPlayer();


watch(canvas, (newCanvas) => {
    if (newCanvas) {
        ctx = newCanvas.getContext("2d");
    }
});


const count = ref(0)
</script>

<template>
    <el-container>
        <el-header id="header_id">
            <h1>泰坦尼克号生存预测</h1>
        </el-header>
        <el-main>
            <div class="radius">
                <Main />
            </div>
            <VideoPlayer />
            <p><span>如果你喜欢的话就在<el-link href="https://github.com/tianhuzong/Titanic.git">→Github←</el-link>上点个star吧</span><br />
            <span>有问题或者有好的建议的话请在github提交<a href="https://github.com/tianhuzong/Titanic/issues">issue</a></span><br />
            <span>Anthor:<a href="https://github.com/tianhuzong/">Github@tianhuzong</a> | <a href="https://space.bilibili.com/3494354284972407">bilibili</a> | <a href="http://afdian.net/a/thzsen">爱发电</a></span></p>
            <span>Copyright Sen 2024</span>
        </el-main>
        <el-footer>

        </el-footer>
    </el-container>
</template>

<style scoped>
.read-the-docs {
    color: #888;
}
.radius {
    width: 60%;
    border: 1px solid #4C4D4F;
    border-radius: 4px;
    margin-top: 30px;
    margin-left: calc((100% - 60%) / 2);
    margin-bottom: 10px;
    padding-top: 20px;
}

</style>
