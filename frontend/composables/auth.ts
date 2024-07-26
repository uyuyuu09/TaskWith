import { defineStore } from 'pinia';
import { getCookie, setCookie } from '~/composables/cookie';
import { callLogin } from '~/composables/user';

export const useUserStore = defineStore('user', {
    state: () => ({
        isLoggedIn: false,
        user: null,
    }),
    getters: {
        loggedInUser(state) {
            return state.user;
        },
    },
    actions: {
        async login(email: string, password: string) {
            try {
                const { accessToken, userData } = await callLogin(email, password) as { accessToken: string, userData: any };
                if (accessToken) {
                    this.isLoggedIn = true;
                    this.user = userData;
                    setCookie('accessToken', accessToken);
                } else {
                    throw new Error('ログインに失敗しました。');
                }
            } catch (error) {
                console.error('ログインエラー:', error);
            }
        },
        async logout() {
            setCookie('accessToken', '', -1);
            this.isLoggedIn = false;
            this.user = null;
        },
    },
    persist: true,
});