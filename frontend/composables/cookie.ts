export function setCookie(name: string, value: string, expires?: number) {
    const date = new Date();
    date.setTime(date.getTime() + (expires || 3600) * 1000);
    const cookieExpires = "expires=" + date.toUTCString();
    document.cookie = `${name}=${value}; ${cookieExpires}; path=/`;
}

export function getCookie(name: string) {
    const cookie = document.cookie;
    const parts = cookie.split('; ');
    for (const part of parts) {
        if (part.startsWith(name + '=')) {
            return part.split('=')[1];
        }
    }
    return null;
}
