<script setup lang="ts">
	const { $pwa } = useNuxtApp();
	const showInstall = ref(true);
	const dismiss = async () => {
		showInstall.value = false;
	};
	const install = async () => {
		$pwa?.install();
	};
</script>

<template>
    <div class="min-h-screen">
            <header class="header text-gray-600 body-font sticky top-0">
                <div class="mx-auto flex flex-wrap p-2 md:flex-row items-center">
                    <div class="items-center my-1 ">
                        <section>
                            <img class="mypass_text" src="~/public/TaskWith.webp" alt="TaskWIth ~Every Day With You~" id="logo">
                        </section>
                    </div>
                </div>
            </header>
            <div class="p-6 w-full">
                    <div v-if="$pwa?.isPWAInstalled == false && showInstall == true" class="flex sm:hidden w-full bg-neutral rounded-xl px-4 py-2 my-4 mb-10 text-sm items-center justify-center">
                        <div class="flex-1">PWAインストール</div>
                        <div class="flex-none flex gap-3">
                            <div class="p-1">
                                <button class="btn btn-primary btn-sm" @click="install()">インストール</button>
                            </div>
                            <button class="underline p-1" @click="dismiss()">表示しない</button>
                        </div>
                    </div>
                </div>
        <slot />
    </div>
</template>