<script setup lang="ts">
    import { useUserStore } from '~/composables/auth';

    const userStore = useUserStore();
    onMounted(() => {
        if (userStore.isLoggedIn) {
            console.log("OK");
        } else {
            navigateTo("/topselect");
        }
    });
</script>

<template>
    <div></div>
</template>