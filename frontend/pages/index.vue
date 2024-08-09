<script setup lang="ts">
    import { useUserStore } from '~/composables/auth';
    const userStore = useUserStore();
    const loggedin = ref(false);
    const loggedout = ref(true);

    onMounted(() => {
        if (userStore.isLoggedIn) {
            loggedin.value = true;
            loggedout.value = false;
        }
    })
</script>

<template>
    <p v-if="loggedin" class="texts flex flex-col items-center justify-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl" id="text">
      <strong>
          <span>{{ String(getCookie("email")).split("@")[0] }}さん こんにちは。</span>
      </strong>
    </p>
    <p v-if="loggedout" class="texts flex flex-col items-center justify-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl" id="text">
      <strong>
          <span>ようこそ TaskWithへ。</span>
      </strong>
    </p>
</template>