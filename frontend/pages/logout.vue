<script setup lang="ts">
import { useUserStore } from '~/composables/auth';
const userStore = useUserStore()
await userStore.logout()
navigateTo("/")
definePageMeta({
    layout: false,
});
</script>
<template>
    <section class="flex flex-col items-center justify-center px-4 py-8 mx-auto lg:py-0" style="height: 100svh;">
        <svg class="fill-blue-600 flex flex-col items-center justify-center mx-auto" width="48" height="48"
            viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <g class="spinner_auJJ">
                <circle class="load" cx="12" cy="3" r="1" />
                <circle class="load load_2" cx="16.50" cy="4.21" r="1" />
                <circle class="load load_3" cx="7.50" cy="4.21" r="1" />
                <circle class="load load_4" cx="19.79" cy="7.50" r="1" />
                <circle class="load load_5" cx="4.21" cy="7.50" r="1" />
                <circle class="load load_6" cx="21.00" cy="12.00" r="1" />
                <circle class="load load_7" cx="3.00" cy="12.00" r="1" />
                <circle class="load load_8" cx="19.79" cy="16.50" r="1" />
                <circle class="load load_9" cx="4.21" cy="16.50" r="1" />
                <circle class="load load_10" cx="16.50" cy="19.79" r="1" />
                <circle class="load load_11" cx="7.50" cy="19.79" r="1" />
                <circle class="load load_12" cx="12" cy="21" r="1" />
            </g>
        </svg>
        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl p-2">
            ログアウトしています
        </h1>
    </section>
</template>