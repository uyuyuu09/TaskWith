import { getCookie } from '~/composables/cookie';

export async function create_events(event_name: string, start_time: string, end_time: string, memo: string) {
    const Token = getCookie('token');
    const create_event = await fetch("http://192.168.0.41:8000/events/create_event", {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${Token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            event_name: event_name,
            start_time: start_time,
            end_time: end_time,
            memo: memo
        })
    });
    if (!create_event.ok) {
        throw new Error(`HTTP error status: ${create_event.status}`);
    }
    return
}