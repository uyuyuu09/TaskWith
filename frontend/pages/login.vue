<script lang="ts" setup>
    import { validateFormData } from '~/composables/validation';
    import { useUserStore } from '~/composables/auth';
    const userStore = useUserStore();
    const email = ref("");
    const password = ref("");
    const email_validation = ref("")
    const password_validation = ref("");
    const email_error_message = ref("");
    const password_error_message = ref("");
    const loginfailed_message = ref("ログインに失敗しました。TaskWithアカウントを作成済みであることを確認し、再度お試しください。");
    const loginUser = async (event: any) => {
        event.preventDefault();
        const validationResult = validateFormData(email.value, password.value);
        if (validationResult.isCurrentEmail && validationResult.inCurrentPassword) {
            email_validation.value = "";
            password_validation.value = "";
            email_error_message.value = "";
            password_error_message.value = "";
            try {
                await userStore.login(email.value, password.value);
                navigateTo("/");
            } catch (error) {
                console.log("NOOOOOO");
                alert(loginfailed_message);
            };
            navigateTo("/");
        } else if (validationResult.isCurrentEmail && !validationResult.inCurrentPassword) {
            email_validation.value = "";
            password_validation.value = "form_validation_error";
            email_error_message.value = ""
            password_error_message.value = "パスワードは8文字以上にしてください。"
        } else if (!validationResult.isCurrentEmail && validationResult.inCurrentPassword) {
            email_validation.value = "form_validation_error";
            password_validation.value = "";
            email_error_message.value = "有効なメールアドレスを入力してください。"
            password_error_message.value = "";
        } else if (!validationResult.isCurrentEmail && !validationResult.inCurrentPassword) {
            email_validation.value = "form_validation_error";
            password_validation.value = "form_validation_error";
            email_error_message.value = "有効なメールアドレスを入力してください。";
            password_error_message.value = "パスワードは8文字以上にしてください。";
        };
    };
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
            <div class="w-full max-w-xs md:max-w-md bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        TaskWithアカウントにログイン
                    </h1>
                    <form class="space-y-4 md:space-y-6" method="post">
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">メールアドレス</label>
                            <input v-model="email" :class="{ 'form_validation_error': email_validation === 'form_validation_error' }" type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="有効なメールアドレスを入力" autocomplete="username">
                            <p class="text-xs">{{ email_error_message }}</p>
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">パスワード</label>
                            <input v-model="password" :class="{ 'form_validation_error': password_validation === 'form_validation_error' }" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" autocomplete="current-password">
                            <p class="text-xs">{{ password_error_message }}</p>
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                            </div>
                            <a href="#" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">パスワードを忘れた場合</a>
                        </div>
                        <button @click="loginUser($event)" type="submit" class="w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">ログイン</button>
                        <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                            TaskWithアカウントをお持ちではない場合: <nuxt-link to="/signup" class="font-medium text-primary-600 hover:underline dark:text-primary-500">アカウントを作成</nuxt-link>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>
