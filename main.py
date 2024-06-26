import gradio as gr
import qrcode 
import qrcode.constants
import qrcode.image.svg

def generate_qr_code(link, box_size, border, fill_color, type):
    qr=qrcode.QRCode(version=1,box_size=box_size,border=border)
    qr.add_data(link)
    qr.make(fit=True)

    print(type)
    if(len(type)==1 and type[0]=='png'):
        img=qr.make_image(fill_color=fill_color)
        img.save("code.png")
        return ("code.png")
    elif(len(type)==1):
        img=qrcode.image.svg.SvgPathImage
        img=qrcode.make(link)
        img.save("code.svg")
        return("code.svg")
    else:
        return

if __name__=='__main__':
    with gr.Blocks() as demo:

        gr.Markdown("# QR-Code generator")

        with gr.Row():
            with gr.Column():
                link=gr.Textbox(label='link')
                box_size=gr.Slider(minimum=1, maximum=100, value=20, step=1, label="Box size")
                border=gr.Slider(minimum=1, maximum=100, value=2, step=1, label="Border")
                with gr.Row():
                    fill_color=gr.ColorPicker(label='Fill color')
                    type=gr.Checkboxgroup(label='Type', choices=['png','svg'])
            code=gr.Image(label='QR-Code',)
        generate=gr.Button('Generate')
        
        generate.click(fn=generate_qr_code, inputs=[link, box_size, border, fill_color, type], outputs=[code])
    demo.launch(share=False)

