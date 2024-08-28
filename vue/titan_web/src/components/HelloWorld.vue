<script setup>
import { ref, watch } from 'vue'
import * as titanUtil from "../utils"
import Main from "./Main.vue"
import {useVideoPlayer} from "../useVideoPlayer.js";
import VideoPlayer from "./VideoPlayer.vue";

const {canvas, play} = useVideoPlayer();

defineProps({
    msg: String,
})

watch(canvas, (newCanvas) => {
    if (newCanvas) {
        ctx = newCanvas.getContext("2d");
    }
});


const count = ref(0)
</script>

<template>
    <div class="radius">
        <Main />
    </div>
    <VideoPlayer />



</template>

<style scoped>
.read-the-docs {
    color: #888;
}
.radius {
    width: 80%;
    border: 1px solid #4C4D4F;
    border-radius: 4px;
    margin-top: 20px;
    margin-left: calc((100% - 80%) / 2);
    margin-bottom: 20px;
    padding-top: 20px;
}
</style>
