<script setup lang="ts">
    import { useUserStore } from '~/composables/auth';

    const userStore = useUserStore();
    onMounted(() => {
        if (userStore.isLoggedIn && getCookie("token") && getCookie("email") && getCookie("password") ) {
            console.log("User loggined. Welcome to TaskWith App!");
        } else {
            navigateTo("/topselect");
        }
    });
</script>

<template>
    <div></div>
</template>