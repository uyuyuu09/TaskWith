<script lang="ts" setup>
    import { validateFormData } from '~/composables/validation';
    import { useUserStore } from '~/composables/auth';
    import { create_events } from '~/composables/events';
    const userStore = useUserStore();
    const event_name = ref("");
    const start_time = ref("");
    const end_time = ref("");
    const memo = ref("");

    const newUser = async (event: any) => {
        event.preventDefault();
        try{
            await create_events(event_name.value, start_time.value, end_time.value, memo.value)
        } catch {
            window.alert("error")
        }
    }
    definePageMeta({
        layout: false,
    });
</script>

<template>
    <section>
        <div class="flex flex-col items-center justify-center px-4 py-8 mx-auto lg:py-0" style="height: 100svh;">
            <p class="flex items-center mb-6 text-3xl font-semibold text-gray-900">
                <img class="taskwith_logo" src="~/public/TaskWith.webp" alt="TaskWith ~Every Day With You~" id="logo">
            </p>
            <div class="w-full max-w-xs md:max-w-md bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                        新規予定を登録
                    </h1>
                    <form class="space-y-4 md:space-y-6" method="post">
                        <div>
                            <label for="event_name" class="block mb-2 text-sm font-medium text-gray-900">予定名</label>
                            <input v-model="event_name"  type="text" name="event_name" id="event_name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" placeholder="予定の名前を入力" autocomplete="off">
                        </div>
                        <div>
                            <label for="start_time" class="block mb-2 text-sm font-medium text-gray-900">開始日時</label>
                            <input v-model="start_time" type="datetime-local" name="start_time" id="start_time" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" autocomplete="off">
                        </div>
                        <div>
                            <label for="end_time" class="block mb-2 text-sm font-medium text-gray-900">終了日時</label>
                            <input v-model="end_time" type="datetime-local" name="end_time" id="end_time" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" autocomplete="off">
                        </div>
                        <div>
                            <label for="memo" class="block mb-2 text-sm font-medium text-gray-900">メモ・備考</label>
                            <textarea v-model="memo" type="text" name="memo" id="memo" placeholder="備考を入力" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" autocomplete="off"></textarea>
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input type="checkbox" class="w-5 h-5 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300" required>
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-gray-500">前日にLINEで通知を受け取る</label>
                                </div>
                            </div>
                        </div>
                        <button @click="newUser($event)" type="submit" class="flex items-center mx-auto justify-center w-1/2 font-medium text-sm px-5 py-2.5 text-center bg-blue-600 text-white hover:bg-blue-800 rounded-lg">
                            送信
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>
