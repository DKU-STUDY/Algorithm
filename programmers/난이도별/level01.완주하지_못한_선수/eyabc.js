function solution (participant, completion) {
    participant.sort();
    completion.sort();

    const participant_len = participant.length;
    let i = 0;
    while(i < participant_len) {
        if (participant[i] !== completion[i])
            return participant[i];
        i++;
    }
}

const JSTestModule = require('/Users/ey/DKU/Algorithm/JSTestModule.js');
JSTestModule('/Users/ey/DKU/Algorithm/programmers/난이도별/level01.완주하지_못한_선수/test.json', solution);