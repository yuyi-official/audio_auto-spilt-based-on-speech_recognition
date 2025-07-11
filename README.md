# audio_auto-spilt-based-on-speech_recognition

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



#作为中国大陆用户，建议在运行此代码前先开启VPN
#因为Google API可能在中国大陆无法正常使用
#运行此代码前请确保已安装所需库：pydub、speech_recognition 以及 ffmpeg

#安装ffmpeg时，请勿使用"pip install ffmpeg"命令
#请从官方网站(https://ffmpeg.org/download.html)
#下载ffmpeg可执行文件并添加到系统PATH中

#此代码基于Python 3.12开发，并在Windows 10/11系统测试通过
#请确保您的系统环境兼容Python 3.12或更高版本

#此代码用于将WAV音频文件按静音分割成多个片段，对每个片段进行语音识别
#并将音频片段及其对应的文字识别结果保存到指定输出目录
#输出目录将包含分割后的音频文件及带时间戳的list文件

#请确保对指定目录具有文件读写权限

#警告：此代码为极简版本，无法替代专业音频处理工作
#特别在AI相关程序中不建议使用此代码





#以下の内容はAIによって翻訳されたものです。


#中国本土のユーザーとして、このコードを実行する前にVPNを有効にすることをお勧めします  
#Google APIが中国本土では正常に動作しない可能性があるためです  
#このコードを実行する前に、必要なライブラリ（pydub、speech_recognition、ffmpeg）がインストールされていることを確認してください  

#「pip install ffmpeg」コマンドを使用してffmpegをインストールするのは避けてください  
#代わりに、公式サイト（https://ffmpeg.org/download.html）
#からffmpegの実行可能ファイルをダウンロードし、システムのPATHに追加してください  

#このコードはPython 3.12で開発され、Windows 10および11でテストされています  
#システム環境がPython 3.12以降と互換性があることを確認してください  

#このコードは、無音に基づいてWAVオーディオファイルをチャンクに分割し、各チャンクの音声認識を行い、  
#指定された出力ディレクトリにチャンクとその対応する文字起こし結果を保存するためのものです  
#出力ディレクトリには、分割されたオーディオファイルとタイムスタンプ付きのリストファイルが含まれます  

#指定されたディレクトリへのファイルの読み書き権限があることを確認してください  

#警告：このコードは非常に最小限のバージョンであり、専門的な音声処理作業の代替とはなりません  
#特にAI関連のプログラムではこのコードの使用を推奨しません  


# -*- coding: utf-8 -*-
