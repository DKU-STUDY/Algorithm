const timeToHM = (time) => time.split(':').map(v => Number(v));

const parseSchedules = (schedules) =>
    schedules.map(schedule => {
        const [bread_time, bread_number] = schedule.split(' ');
        const [bread_hour, bread_min] = timeToHM(bread_time);
        return [bread_hour, bread_min, bread_number];
    });

const getTakesTime = (current_time, last_time) => {
    const [current_hour, current_min] = current_time;
    const [last_hour, last_min] = last_time;

    if (current_hour === last_hour && current_min === last_min) return 0;

    const current = new Date(2020, 7, 23, ...current_time);
    const last = new Date(2020, 7, 23, last_hour, last_min);
    return Math.floor((last.getTime() - current.getTime()) / 60000);
};

const getBreakTime = (schedules, K, current_hour, current_min) => {
    const schedule_length = schedules.length;
    let breakTime;

    for (let i = 0 ; i < schedule_length ; i++) {
        const [bread_hour, bread_min, bread_number] = schedules[i];
        if (K < 1) {
            breakTime = i - 1;
            break;
        }

        if ((bread_hour < current_hour)
            || (bread_hour === current_hour && bread_min < current_min))
            continue;
        K -= bread_number;
    }
    return [breakTime || (schedule_length - 1), K];
};

function solution (bakery_schedule, current_time, K) {
    current_time = timeToHM(current_time);
    const [current_hour, current_min] = current_time;
    const schedules = parseSchedules(bakery_schedule);

    const [breakTime, remain_break] = getBreakTime(schedules, K, current_hour, current_min);
    if (remain_break > 0) return -1;

    const last_time = schedules[breakTime];
    return getTakesTime(current_time, last_time);

}

console.log(
    solution(['09:05 10', '12:20 5', '13:25 6', '14:24 5'], '12:05', 10) === 80,
    solution(['12:00 10'], '12:00', 10) === 0,
    solution(['12:00 10'], '12:00', 11) === -1,
);


