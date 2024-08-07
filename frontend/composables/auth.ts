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
                // const { accessToken, userData } = await callLogin(email, password) as { accessToken: string, userData: any };
                const { token, userData } = await callLogin(email, password) as { token: string, userData: any };
                if (token) {
                    // console.log("token:" + token)
                    this.isLoggedIn = true;
                    this.user = userData;
                    // setCookie('accessToken', accessToken);
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
            maxAge: 604800,
        }),
    },
});

// export const useUserStore = defineStore('user',
//     () => {
//         const token = ref<string | null>(null);
//         function setToken(new_user: string) {
//             token.value = new_user;
//         }
//         function clearToken() {
//             token.value = null;
//         }
//         return { token, setToken, clearToken }
//     },
//     {
//         persist: {
//             storage: persistedState.cookiesWithOptions({
//                 sameSite: 'strict',
//                 maxAge: 604800,
//             }),
//         },
//     }
// );