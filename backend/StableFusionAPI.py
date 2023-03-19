import requests


class StableFusionAPI:
    def __init__(self):
        self.url = "http://bncukaybbrp4mdch66m3qvs2jqskv65bykw7pwt5n6yzleiya5ha.remote.moe"

    def txt2img(self, text):
        print(self.url)
        endpoint = "/sdapi/v1/txt2img"
        request_body = {
            "enable_hr": False,
            "denoising_strength": 0,
            "firstphase_width": 0,
            "firstphase_height": 0,
            "hr_scale": 2,
            "hr_upscaler": "string",
            "hr_second_pass_steps": 0,
            "hr_resize_x": 0,
            "hr_resize_y": 0,
            "prompt": f'ghibli style, ${text}',
            "seed": -1,
            "subseed": -1,
            "subseed_strength": 0,
            "seed_resize_from_h": -1,
            "seed_resize_from_w": -1,
            "batch_size": 3,
            "n_iter": 1,
            "steps": 35,
            "cfg_scale": 7,
            "width": 512,
            "height": 512,
            "restore_faces": True,
            "tiling": False,
            "do_not_save_samples": False,
            "do_not_save_grid": False,
            "negative_prompt": "string",
            "eta": 0,
            "s_churn": 0,
            "s_tmax": 0,
            "s_tmin": 0,
            "s_noise": 1,
            "override_settings": {},
            "override_settings_restore_afterwards": True,
            "script_args": [],
            "sampler_index": "Euler",
            "send_images": True,
            "save_images": False,
            "alwayson_scripts": {}
        }
        return requests.post(self.url + endpoint, json=request_body)
