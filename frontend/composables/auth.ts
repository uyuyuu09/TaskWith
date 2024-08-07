import { defineStore } from 'pinia';
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
                const { token, userData } = await callLogin(email, password) as { token: string, userData: any };
                if (token) {
                    this.isLoggedIn = true;
                    this.user = userData;
                    console.log("auth:" + token, userData.email)
                    return { token, userData }
                } else {
                    throw new Error('ログインに失敗しました。');
                }
            } catch (error) {
                console.error('ログインエラー:', error);
            }
        },
        async logout() {
            setCookie('accessToken', '');
            this.isLoggedIn = false;
            this.user = null;
        },
    },
    persist: {
        storage: persistedState.cookiesWithOptions({
            sameSite: 'strict',
            maxAge: 60 * 60,
        }),
    },
});
