<template>
    <div>
        <canvas ref="canvas" width="640" height="360" id='canvas_player'></canvas>
    </div>
</template>

<script setup>
import {useVideoPlayer} from "../useVideoPlayer.js"

const {canvas, play} = useVideoPlayer();
//console.log("视频播放组件中:",canvas.value);
</script>

<style scoped>
canvas {
    border: 1px solid #fffff;

}
</style>
