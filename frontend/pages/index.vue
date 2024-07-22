<script setup lang="ts">
    import { ref, onMounted } from 'vue';

    const calendarContent = ref(null);

    const fetchData = async () => {
        const all = await fetch('http://127.0.0.1:8000/user/id')
        const response = await fetch('http://127.0.0.1:8000/user/calendar', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
            id: "c_7d7179e8a57398a79e70d4d38f64c9bd71704e01af3c45bb048e6bd58ab3cd63@group.calendar.google.com",
            })
        });

        calendarContent.value = await response.json();
    };

    onMounted(fetchData);
</script>

<template>
  <div v-if="calendarContent && calendarContent.data">
    <ul>
      <li v-for="(item, index) in calendarContent.data" :key="index">
        {{ item.開始時間 }} - {{ item.イベント名 }}
      </li>
    </ul>
  </div>
</template>
