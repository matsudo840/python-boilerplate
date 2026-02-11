"""
メインモジュール

このモジュールはGradioを用いたチャットアプリケーションを提供します。
ユーザが入力したメッセージに対して、ランダムな相槌応答を返します。
"""

import random
import gradio as gr

RESPONSES = [
    "そうですね！",
    "本当ですか？",
    "なるほど～",
    "へぇ、そうなんですね！",
    "うん、うん。"
]

def chat(message, history=None):
    """チャット処理関数

    Args:
        message (str): ユーザからの入力メッセージ
        history (list of tuple, optional): チャット履歴。初回はNone

    Returns:
        tuple: 更新されたチャット履歴、およびGradio用ステートの出力
    """
    if history is None:
        history = []
    reply = random.choice(RESPONSES)
    history.append((message, reply))
    return history, history

def main():
    """Gradioチャットアプリケーションを起動する"""
    with gr.Blocks() as demo:
        gr.Markdown("# チャットアプリ")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="メッセージを入力してください...")
        clear = gr.Button("クリア")
    
        msg.submit(chat, [msg, chatbot], [chatbot, msg])
        clear.click(lambda: ([], []), None, [chatbot, msg])
    
    demo.launch()

if __name__ == "__main__":
    main()
