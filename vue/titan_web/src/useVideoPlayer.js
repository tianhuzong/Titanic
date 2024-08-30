// useVideoPlayer.js
import { ref, onMounted } from 'vue';
import {ElMessageBox} from "element-plus";
export function useVideoPlayer() {

    window.canvas = ref(null);
    //window.canvas._value = document.getElementById("canvas_player")[0];
    let videoEl = null;
    let ctx = null;


    const play = (callback = null, videosrc = "/sence1.mp4") => {
        if (callback === null) {
                callback = () => {
                console.log("视频播放结束");
            };
        }
        
        videoEl.addEventListener("ended", function () {
            callback();
            ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);
            ctx = null;
            var targetElement = document.getElementById('header_id');

            // 使用scrollIntoView方法平滑滚动到目标元素
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }

        });
        var targetElement = document.getElementById('canvas_player');

        // 使用scrollIntoView方法平滑滚动到目标元素
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
        videoEl.src = videosrc;
        videoEl.load();
        videoEl.currentTime = 0;
        canvas.value = document.getElementById("canvas_player");
        ctx = canvas.value.getContext("2d");
        debugger;
        if (ctx) {
            console.log("start videoRender");
            videoEl.play();
            videoRender();

            debugger;
        }
    };

    const videoRender = () => {
        if (ctx) {
            console.log("videoRender");
            ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);
            ctx.drawImage(videoEl, 0, 0, canvas.value.width, canvas.value.height);
            window.requestAnimationFrame(videoRender);
        }
    };

    onMounted(() => {
      // 创建一个虚拟video元素

        videoEl = document.createElement("video");
        

        // 重要：由于浏览器限制自动播放问题，则需要使用无声播放即可实现自动播放
        videoEl.muted = false;
        videoEl.loop = false;

        // 获取canvas元素和上下文
        if (canvas.value) {
            console.log("canvas:", canvas.value);
            ctx = canvas.value.getContext("2d");
        }
      });
      const cas = window.canvas
      return {
          cas,
          play
      };
}
