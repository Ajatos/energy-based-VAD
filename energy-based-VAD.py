import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
sr, data = wavfile.read("녹음.wav")

#제곱합제곱근(L2 노름)
def l2_norm(frames):
    return np.sum(frames**2,axis=1)**0.5

#짧은 소리(잡음) 제거하기
def remove_shorts_speech(vad,max_len):
    vad = vad.copy()
    n = 0
    for i in range(len(vad)):
        a = vad[i]
        if a == 1:
            n = n+1
        elif n > 0:
            if n <= max_len:
                vad[i-n: i] = 0
                n = 0
            else:
                n = 0
    if n>0 and max_len >= n:
        vad[len(vad) - n:] = 0
    return vad

#빈 소리 채우기
def frll_shorts_void(vad,max_len): #오타 아님, 아무튼 아님
    vad = vad.copy()
    n = 0
    m = 0
    for i in range(len(vad)):
        a = vad[i]
        if a == 0:
            n = n+1
        elif n > 0:
            if n <= max_len:
                if m==0:
                    n=0
                else:
                    vad[i-n: i] = 1
                    n = 0
            else:
                n = 0
        if a == 1:
            m = 1
    return vad

#프레임(0.02초)당 길이 구하기
frame_len = int(sr * 0.02)

#프레임 개수 구하기
n_frame = int(len(data)//frame_len)

#안쓰는 프레임 버리기(프레임 맞추기)
data = data[:int(n_frame*frame_len)]

#데이터 프레임 단위 정렬
data = data.reshape(n_frame,frame_len)

#data값 전부 실수로 바꿔주기
data = data.astype(float)

#이진으로 발화 여부 계산
l2_data = l2_norm(data)
mean = np.mean(l2_data)
vad = l2_data > mean
vad = vad.astype(int)

#음 채우기
clean_data = frll_shorts_void(vad,5)

#잡음제거
full_clean_data = remove_shorts_speech(clean_data,5)

#그래프로 나타내기
final_data = full_clean_data*l2_data.max()
y = np.arange(0, n_frame, 1)* frame_len / sr
plt.plot(y, l2_data, label='Signal energy')
plt.plot(y, final_data, label='VAD decision')
plt.ylabel("energy")
plt.xlabel("time(s)")
plt.axhline(y=mean,linestyle="--",label='Threshold',color='black')
plt.title('energy-based-VAD')
plt.legend()
plt.show()