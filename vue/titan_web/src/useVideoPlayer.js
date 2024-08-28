// useVideoPlayer.js
import { ref, onMounted } from 'vue';
export function useVideoPlayer() {
  
  window.canvas = ref(null);
  //window.canvas._value = document.getElementsByTagName("canvas")[0];
  console.log("滴流盒",window.canvas.value);
  let videoEl = null;
  let ctx = null;
  let isPlaying = false;

  const play = () => {
    canvas.value = document.getElementsByTagName("canvas")[0];
    ctx = canvas.value.getContext("2d");
    debugger;
    if (!isPlaying && ctx) {
      console.log("play",ctx);
      console.log(canvas.value);
      videoEl.play();
      isPlaying = true;
      videoRender();
      debugger;
    }
  };

  const videoRender = () => {
    if (isPlaying && ctx) {
      ctx.clearRect(0, 0, canvas.value.width, canvas.value.height);
      ctx.drawImage(videoEl, 0, 0, canvas.value.width, canvas.value.height);
      window.requestAnimationFrame(videoRender);
    }
  };

  onMounted(() => {
    // 创建一个虚拟video元素
    
    videoEl = document.createElement("video");
    videoEl.src = 'https://upos-sz-mirrorali.bilivideo.com/upgcxcode/44/45/1025814544/1025814544-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1724834286&gen=playurlv2&os=alibv&oi=17627301&trid=d574cb22648a4647aec9fa564b24b47fh&mid=0&platform=html5&og=hw&upsig=88f5a8ee47a40549529e8c2892adfd89&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&f=h_0_0&bw=52622&logo=80000000'; // 确保路径正确

    // 重要：由于浏览器限制自动播放问题，则需要使用无声播放即可实现自动播放
    videoEl.muted = true;
    videoEl.loop = true;

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
