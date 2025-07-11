#As a China main land users, it is recommended to enable VPN before running this code
#Because the Google API may not work in China mainland.
#Before running this code, please ensure you have installed the required libraries:pydub, speech_recognition, and ffmpeg.

#Avoid using "pip install ffmpeg" command to install ffmpeg.
#Instead, download the ffmpeg executable from the official website (https://ffmpeg.org/download.html) and add it to your system's PATH.

#This code is built by Python 3.12 and tested on windows 10 and 11.
#Please ensure your system environment is compatible with Python 3.12 or later versions.


#This code is designed to split a WAV audio file into chunks based on silence, recognize speech in each chunk,
#and save the chunks and their corresponding transcriptions in a specified output directory.
#The output directory will contain the audio chunks and a list file with the start and end times


#Please ensure you have the necessary permissions to read and write files in the specified directories.

#Warning:This code just a very minimalist version.Cann't replace people's work in Audio processing.Especially in AI programe.

# 作为中国大陆用户，建议在运行此代码前先开启VPN
# 因为Google API可能在中国大陆无法正常使用
# 运行此代码前请确保已安装所需库：pydub、speech_recognition 以及 ffmpeg

# 安装ffmpeg时，请勿使用"pip install ffmpeg"命令
# 请从官方网站(https://ffmpeg.org/download.html)下载ffmpeg可执行文件并添加到系统PATH中

# 此代码基于Python 3.12开发，并在Windows 10/11系统测试通过
# 请确保您的系统环境兼容Python 3.12或更高版本

# 此代码用于将WAV音频文件按静音分割成多个片段，对每个片段进行语音识别
# 并将音频片段及其对应的文字识别结果保存到指定输出目录
# 输出目录将包含分割后的音频文件及带时间戳的list文件

# 请确保对指定目录具有文件读写权限

# 警告：此代码为极简版本，无法替代专业音频处理工作
# 特别在AI相关程序中不建议使用此代码


#以下の内容はAIによって翻訳されたものです。


#中国本土のユーザーとして、このコードを実行する前にVPNを有効にすることをお勧めします  
#Google APIが中国本土では正常に動作しない可能性があるためです  
#このコードを実行する前に、必要なライブラリ（pydub、speech_recognition、ffmpeg）がインストールされていることを確認してください  

#「pip install ffmpeg」コマンドを使用してffmpegをインストールするのは避けてください  
#代わりに、公式サイト（https://ffmpeg.org/download.html）からffmpegの実行可能ファイルをダウンロードし、システムのPATHに追加してください  

#このコードはPython 3.12で開発され、Windows 10および11でテストされています  
#システム環境がPython 3.12以降と互換性があることを確認してください  

#このコードは、無音に基づいてWAVオーディオファイルをチャンクに分割し、各チャンクの音声認識を行い、  
#指定された出力ディレクトリにチャンクとその対応する文字起こし結果を保存するためのものです  
#出力ディレクトリには、分割されたオーディオファイルとタイムスタンプ付きのリストファイルが含まれます  

#指定されたディレクトリへのファイルの読み書き権限があることを確認してください  

#警告：このコードは非常に最小限のバージョンであり、専門的な音声処理作業の代替とはなりません  
#特にAI関連のプログラムではこのコードの使用を推奨しません  


# -*- coding: utf-8 -*-
'''
created on 2025/07/19 19:30:21

created by: YUYI
'''

import os
import wave
import contextlib
import shutil
from pydub import AudioSegment, silence
import speech_recognition as sr


def split_audio_by_silence(input_wav, output_dir, min_silence_len=500, silence_thresh=-40):
    audio = AudioSegment.from_wav(input_wav)
    chunks = silence.split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
        keep_silence=200
    )
    return chunks

def get_chunk_times(input_wav, chunks):
    audio = AudioSegment.from_wav(input_wav)
    times = []
    start = 0
    for chunk in chunks:
        duration = len(chunk)
        end = start + duration
        times.append((start, end))
        start = end
    return times

def recognize_speech_from_chunk(chunk, lang='zh-CN'):
    recognizer = sr.Recognizer()
    with sr.AudioFile(chunk) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=lang)
    except Exception:
        text = "未识别"
    return text

def save_chunks_and_list(input_wav, output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    chunks = split_audio_by_silence(input_wav, output_dir)
    times = get_chunk_times(input_wav, chunks)
    recognizer = sr.Recognizer()
    list_lines = []


    for idx, (chunk, (start, end)) in enumerate(zip(chunks, times)):
        chunk_filename = os.path.join(output_dir, f"chunk_{idx}.wav")
        chunk.export(chunk_filename, format="wav")


        with sr.AudioFile(chunk_filename) as source:
            audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language="zh-CN")
        except Exception:
            text = f"未识别_{idx}"


        safe_text = "".join([c if c.isalnum() or c in "_-" else "_" for c in text])
        wav_name = os.path.join(output_dir, f"{safe_text}.wav")
        orig_wav_name = wav_name
        count = 1
        while os.path.exists(wav_name):
            wav_name = os.path.join(output_dir, f"{safe_text}_{count}.wav")
            count += 1
        if wav_name != orig_wav_name:
            print(f"[运行状态] 文件重名，已重命名为: {os.path.basename(wav_name)}")
        else:
            print(f"[运行状态] 文件保存为: {os.path.basename(wav_name)}")
        os.rename(chunk_filename, wav_name)


        list_lines.append(f"{start/1000:.2f}-{end/1000:.2f} {text}")


    list_path = os.path.join(output_dir, "xx.list")
    with open(list_path, "w", encoding="utf-8") as f:
        for line in list_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    input_wav = "H:\\FFOutput\\2.wav"  # 输入的wav文件路径 #input your wav file path
    output_dir = "H:\\FFOutput\\test2"  # 输出文件夹 #input your output dir path
    print("Please wait!The program is loading...")
    save_chunks_and_list(input_wav, output_dir)