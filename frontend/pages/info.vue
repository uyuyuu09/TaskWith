<script setup lang="ts">
    const display_time = ref("");
    const intervalId = ref<number | null>(null);
    onMounted(() => {
        intervalId.value = window.setInterval(() => {
            let nowTime = new Date();
            let nowYoubi = ["日", "月", "火", "水", "木", "金", "土"][nowTime.getDay()];
            let nowHour = set2fig(nowTime.getHours());
            let nowMin = set2fig(nowTime.getMinutes());
            let nowSec = set2fig(nowTime.getSeconds());
            let currentTime = `${nowTime.getMonth() + 1}/${nowTime.getDate()} (${nowYoubi}) ${nowHour}:${nowMin}:${nowSec}`;
            display_time.value = currentTime;
        }, 100);
    });

    onUnmounted(() => {
        if (intervalId.value!== null) {
            clearInterval(intervalId.value);
        }
    });

    function set2fig(num: Number) {
        return String(num).padStart(2, '0');
    }
</script>

<template>
    <section class="flex justify-center items-center text-gray-600 body-font">
        <div class="container px-5 pb-20 mx-auto">
            <div class="flex flex-col text-center w-full mb-10">
                <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">インフォメーション</h1>
                <p class="lg:w-2/3 mx-auto leading-relaxed text-base">各項目をタップ・クリックすると、該当ページを新規タブで開きます。</p>
            </div>
            <div class="flex flex-wrap -m-2">
                <nuxt-link to="/policy" target="_blank" class="p-2 lg:w-1/3 md:w-1/2 w-full">
                    <div class="h-full flex items-center border-gray-200 border p-4 rounded-lg">
                        <div class="flex-grow">
                            <h2 class="text-gray-900 title-font font-medium">プライバシーポリシー</h2>
                            <p class="text-gray-500">本サイトのプライバシーに関する重要なお知らせです。</p>
                        </div>
                    </div>
                </nuxt-link>
                <nuxt-link to="/account" class="p-2 lg:w-1/3 md:w-1/2 w-full">
                    <div class="h-full flex items-center border-gray-200 border p-4 rounded-lg">
                        <div class="flex-grow">
                            <h2 class="text-gray-900 title-font font-medium">ログイン情報</h2>
                            <p class="text-gray-500">現在のログイン情報を表示します。ログインされていない場合はログイン画面へリンクします。</p>
                        </div>  
                    </div>
                </nuxt-link>
                <nuxt-link to="#" target="_blank" class="p-2 lg:w-1/3 md:w-1/2 w-full">
                    <div class="h-full flex items-center border-gray-200 border p-4 rounded-lg">
                        <div class="flex-grow">
                            <h2 class="text-gray-900 title-font font-medium">管理者ページ</h2>
                            <p class="text-gray-500">本サイトの管理者ページです。</p>
                        </div>
                    </div>
                </nuxt-link>
            </div>
        </div>
    </section>
</template>