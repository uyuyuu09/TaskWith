import { getCookie, setCookie } from '~/composables/cookie';

export async function signUp(email: string, password: string) {
    try {
        const makeUser = await fetch("http://127.0.0.1:8000/users/create", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                // name: "",
                email: email,
                password: password
            })
        });
        if (!makeUser.ok) {
            throw new Error(`HTTP error status: ${makeUser.status}`);
        }
        const getToken = await fetch("http://127.0.0.1:8000/users/token", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });
        if (!getToken.ok) {
            throw new Error(`HTTP error status: ${getToken.status}`);
        }
        const accessToken = await getToken.json();
        setCookie('accessToken', accessToken.access_token);

        let userData: any = null;
        const getAccessToken = getCookie('accessToken');
        if (getAccessToken) {
            const response = await fetch("http://127.0.0.1:8000/users/me", {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${getAccessToken}`
                }
            });
            if (!response.ok) {
                throw new Error(`User data fetch error: ${response.status}`);
            }
            userData = await response.json();
        }
        return { accessToken, userData };
    } catch (error) {
        console.error('Error:', error);
    }
}


export async function callLogin(email: string, password: string) {
    try {
        let userData: any = null;
        const accessToken = getCookie('accessToken') || "none";
        if (accessToken === "none") {
            const getToken = await fetch("http://127.0.0.1:8000/users/token", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            });
            if (!getToken.ok) {
                throw new Error(`HTTP error status: ${getToken.status}`);
            }
            const json_accessToken = await getToken.json();
            const accessToken = json_accessToken.access_token;
            setCookie('accessToken', accessToken);
            const response = await fetch("http://127.0.0.1:8000/users/me", {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${accessToken}`
                }
            });
            if (!response.ok) {
                throw new Error(`User data fetch error: ${response.status}`);
            }
            userData = await response.json();
            // return { accessToken, userData };
        } else {
            const response = await fetch("http://127.0.0.1:8000/users/me", {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${accessToken}`
                }
            });
            if (!response.ok) {
                throw new Error(`User data fetch error: ${response.status}`);
            }
            userData = await response.json();
            console.log(userData);
            // return { accessToken, userData };
        }
        return { accessToken, userData };
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
