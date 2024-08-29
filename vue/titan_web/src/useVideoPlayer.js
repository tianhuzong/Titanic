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

        });
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
        videoEl.src = 'https://cn-sh-ct-01-09.bilivideo.com/upgcxcode/19/44/500001633034419/500001633034419-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1724860551&gen=playurlv2&os=bcache&oi=2672513485&trid=000036302285362047b6a0459e5ffede9d70h&mid=0&platform=html5&og=cos&upsig=cfddedbcf530fc09a734bb6fc5f30f32&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=88209&bvc=vod&nettype=0&f=h_0_0&bw=64117&logo=80000000'; // 确保路径正确

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
