<script setup lang="ts">
    definePageMeta({
        layout: false,
    });
</script>
<template>
    <section>
        <div class="flex flex-col items-center justify-center px-4 py-8 mx-auto lg:py-0" style="height: 100svh;">
            <p class="flex items-center mb-6 text-3xl font-semibold text-gray-900 dark:text-white">
                <img class="mypass_text" src="~/public/TaskWith.webp" alt="TaskWith ~Every Day With You~" id="logo">
            </p>
            <!-- <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white pb-5">
                ようこそ
            </h1> -->
            <div class="w-full max-w-xs md:max-w-md bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <form class="space-y-4 md:space-y-6" method="post">
                        <div>
                            <nuxt-link to="/signUp" class="flex justify-center">初めてご利用する方はこちら</nuxt-link>
                        </div>
                        <div>
                            <nuxt-link to="/login" class="flex justify-center">登録済みの方はこちら</nuxt-link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>