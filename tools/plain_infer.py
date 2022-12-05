import torch

from PIL import Image
import torchvision.transforms as transforms

from smoke.config import cfg
from smoke.engine import (
    default_argument_parser,
    default_setup
)
from smoke.utils.check_point import DetectronCheckpointer
from smoke.modeling.detector import build_detection_model


def setup(args):
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    default_setup(cfg, args)
    return cfg


def main(args):
    cfg = setup(args)

    model = build_detection_model(cfg)
    device = torch.device(cfg.MODEL.DEVICE)
    model.to(device)

    checkpointer = DetectronCheckpointer(cfg, model, save_dir=cfg.OUTPUT_DIR)
    ckpt = cfg.MODEL.WEIGHT if args.ckpt is None else args.ckpt
    _ = checkpointer.load(ckpt, use_latest=args.ckpt is None)

    # Read a PIL image
    image = Image.open('data/kylle-pangan-unsplash.jpg')
    # Define a transform to convert PIL image to a Torch tensor
    # transform = transforms.Compose([
    #     transforms.PILToTensor()
    # ])
    transform = transforms.PILToTensor()
    # Convert the PIL image to Torch tensor
    img_tensor = transform(image)

    img_tensor = img_tensor.to(device)
    output = model(img_tensor)
    cpu_device = torch.device("cpu")
    output = output.to(cpu_device)


if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    print("Command Line Args:", args)
    main(args)

# `python tools/plain_infer.py --eval-only --config-file "configs/smoke_gn_vector.yaml"`