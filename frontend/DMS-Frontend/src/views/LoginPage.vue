<script setup lang="ts">
import Login from "@/components/Login.vue";
import {useRouter} from "vue-router";

const router = useRouter();
const login = () => {
  console.log("Login");
  router.push("/home")
}
</script>

<template>
  <Login @after-login="login"/>
</template>

<style scoped>

</style>