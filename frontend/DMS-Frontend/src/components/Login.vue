<script setup lang="ts">
import {useUserStore} from "@/stores/userStore.ts";
import {reactive} from "vue";
import type {User} from "@/types/user.ts"

const userStore = useUserStore();
const user = reactive<User>({username: '', password: ''});
const emit = defineEmits(["afterLogin"])
const login = async () => {
  await userStore.login(user)
  if (userStore.isLoggedIn) {
    emit("afterLogin");
  }
}
</script>


<template>

  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto"
           src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company"/>
      <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Login</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="email" class="block text-sm/6 font-medium text-gray-900">Username</label>
          <div class="mt-2">
            <InputText v-model="user.username"></InputText>
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>

          </div>
          <div class="mt-2">
            <InputText v-model="user.password"></InputText>
          </div>
        </div>

        <div>
          <!--          <button type="submit"-->
          <!--                  class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">-->
          <!--            Login-->
          <!--          </button>-->
          <Button @click="login" label="Login"></Button>
          <Message v-if="userStore.error" severity="error" :life="3000">Username or Password are wrong</Message>
        </div>
      </form>
    </div>
  </div>

</template>


<style scoped>

</style>