<script setup lang="ts">
    import { useUserStore } from '#imports';
    const userStore = useUserStore();
    const email = ref<string | null>(null)
    const status = ref("")
    const msg = ref("")
    onMounted(() => {
        if (userStore.isLoggedIn && getCookie("token") && getCookie("email") && getCookie("password") ) {
            email.value = getCookie("email");
            status.value = "ログイン";
            msg.value = `アクセスしているメールアドレス: ${email.value}`;
        } else {
            navigateTo("/topselect");
        }
    });
</script>

<template>
    <section>
        <section class="relative pt-36 pb-24">
            <img src="~/public/user_bg.webp" alt="cover-image" class="w-full absolute top-0 left-0 z-0 h-60">
            <div class="w-full max-w-7xl mx-auto px-6 md:px-8">
                <div class="flex items-center justify-center relative z-10 mb-2.5">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="w-20 h-20 mt-12 bg-white border-4 border-solid border-white rounded-full">
                        <path d="M304 128a80 80 0 1 0 -160 0 80 80 0 1 0 160 0zM96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM49.3 464l349.5 0c-8.9-63.3-63.3-112-129-112l-91.4 0c-65.7 0-120.1 48.7-129 112zM0 482.3C0 383.8 79.8 304 178.3 304l91.4 0C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7L29.7 512C13.3 512 0 498.7 0 482.3z"/>
                    </svg>
                </div>
                <h3 class="text-center font-manrope font-bold text-3xl leading-10 text-gray-900 mb-3">
                    {{ email?.split("@")[0] }}
                </h3>
                <p class="font-normal text-base leading-7 text-gray-500 text-center mb-8">
                    {{ email }}
                </p>
                <div class="flex items-center justify-center gap-5">
                    <a href="javascript:;"
                        class="p-3 rounded-full border border-solid border-gray-300 group bg-gray-50 transition-all duration-500 hover:border-indigo-700">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-6 h-6 fill-green-500">
                            <path d="M311 196.8v81.3c0 2.1-1.6 3.7-3.7 3.7h-13c-1.3 0-2.4-.7-3-1.5l-37.3-50.3v48.2c0 2.1-1.6 3.7-3.7 3.7h-13c-2.1 0-3.7-1.6-3.7-3.7V196.9c0-2.1 1.6-3.7 3.7-3.7h12.9c1.1 0 2.4 .6 3 1.6l37.3 50.3V196.9c0-2.1 1.6-3.7 3.7-3.7h13c2.1-.1 3.8 1.6 3.8 3.5zm-93.7-3.7h-13c-2.1 0-3.7 1.6-3.7 3.7v81.3c0 2.1 1.6 3.7 3.7 3.7h13c2.1 0 3.7-1.6 3.7-3.7V196.8c0-1.9-1.6-3.7-3.7-3.7zm-31.4 68.1H150.3V196.8c0-2.1-1.6-3.7-3.7-3.7h-13c-2.1 0-3.7 1.6-3.7 3.7v81.3c0 1 .3 1.8 1 2.5c.7 .6 1.5 1 2.5 1h52.2c2.1 0 3.7-1.6 3.7-3.7v-13c0-1.9-1.6-3.7-3.5-3.7zm193.7-68.1H327.3c-1.9 0-3.7 1.6-3.7 3.7v81.3c0 1.9 1.6 3.7 3.7 3.7h52.2c2.1 0 3.7-1.6 3.7-3.7V265c0-2.1-1.6-3.7-3.7-3.7H344V247.7h35.5c2.1 0 3.7-1.6 3.7-3.7V230.9c0-2.1-1.6-3.7-3.7-3.7H344V213.5h35.5c2.1 0 3.7-1.6 3.7-3.7v-13c-.1-1.9-1.7-3.7-3.7-3.7zM512 93.4V419.4c-.1 51.2-42.1 92.7-93.4 92.6H92.6C41.4 511.9-.1 469.8 0 418.6V92.6C.1 41.4 42.2-.1 93.4 0H419.4c51.2 .1 92.7 42.1 92.6 93.4zM441.6 233.5c0-83.4-83.7-151.3-186.4-151.3s-186.4 67.9-186.4 151.3c0 74.7 66.3 137.4 155.9 149.3c21.8 4.7 19.3 12.7 14.4 42.1c-.8 4.7-3.8 18.4 16.1 10.1s107.3-63.2 146.5-108.2c27-29.7 39.9-59.8 39.9-93.1z"/>
                        </svg>
                    </a>
                </div>
            </div>
        </section>
                                            
    </section>
</template>