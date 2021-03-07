package Divisor_Game;

class HyeonJeong {
    public boolean divisorGame(int N) {
        int state = 0;
        while (N > 1) {
            for (int divisor = 1; divisor < N/2+1; divisor++) {
                if (N%divisor == 0) {
                    N = N-divisor;
                    break;
                }
            }
            state++;
        }
        return (state%2 == 0)?false:true;
    }
}
