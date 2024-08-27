<script setup>
import { ref } from 'vue'
import * as titanUtil from "../utils"
defineProps({
  msg: String,
})

const session = titanUtil.create_session("../../../../py/models/onnx_model/titan.onnx");
const input_data = titanUtil.buildTensor(1, 14, 7.55, "S", 1, "Officer", "A", 11);
const output_data = titanUtil.predict(input_data);
console.log(output_data);

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Learn more about IDE Support for Vue in the
    <a
      href="https://vuejs.org/guide/scaling-up/tooling.html#ide-support"
      target="_blank"
      >Vue Docs Scaling up Guide</a
    >.
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
