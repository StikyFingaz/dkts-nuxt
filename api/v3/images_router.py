from collections import defaultdict
import os
from pathlib import Path
from fastapi import APIRouter, Depends
from pymage_size import get_image_size
from sqlmodel import or_, select, Session
from app_config import settings
from dependencies import get_session
from models.play import Play

"""Provides image-serving endpoints"""

router = APIRouter(
    prefix='/images',
    tags=['images'],
    dependencies=[],  # Add dependencies here
    responses={},  # Add responses here
)

working_dirs = settings.working_dirs
working_env = settings.work_env


@router.get('/main-carousel')
async def fetch_images():
    carousel_cwd = Path(working_dirs[working_env]) / 'media/main-carousel'
    mobile_carousel = [img for img in os.listdir(Path(carousel_cwd) / 'mobile')]
    desktop_carousel = [
        img for img in os.listdir(carousel_cwd) if (Path(carousel_cwd) / img).is_file()
    ]
    carousel_images = {
        'mobileImages': mobile_carousel, 'desktopImages': desktop_carousel
    }

    return carousel_images


@router.get('/highlights')
async def fetch_images(session: Session = Depends(get_session)):
    highlights = session.exec(select(Play).where(or_(
        Play.highlight,
        Play.premiere
    ))).all()

    highlight_covers = defaultdict(tuple)
    for highlight in highlights:
        img_file = f'{working_dirs[working_env]}/media/plays/{highlight.slug}/cover.jpg'
        img_format = get_image_size(img_file)
        width, height = img_format.get_dimensions()
        highlight_covers[highlight.slug] = width, height

    highlight_posters = defaultdict(tuple)
    for highlight in highlights:
        img_file = f'{working_dirs[working_env]}/media/plays/{highlight.slug}/poster.jpg'
        img_format = get_image_size(img_file)
        width, height = img_format.get_dimensions()
        highlight_posters[highlight.slug] = width, height

    return {'covers': highlight_covers, 'posters': highlight_posters}


@router.get('/sponsors')
async def fetch_images():
    sponsors_cwd = f'{working_dirs[working_env]}/sponsors'
    sponsor_logos = defaultdict(tuple)

    for img in os.listdir(sponsors_cwd):
        img_file = f'{sponsors_cwd}/{img}'
        if Path(img_file).is_file():
            img_format = get_image_size(img_file)
            width, height = img_format.get_dimensions()
            sponsor_logos[img] = width, height

    return sponsor_logos


@router.get('/fest-sponsors')
async def fetch_images():
    sponsors_cwd = f'{working_dirs[working_env]}/sponsors/festival'

    return os.listdir(sponsors_cwd)


@router.get('/play-photos/{play_slug}')
async def fetch_play_photos(play_slug: str):
    play_photos_dir = Path(working_dirs[working_env]) / f'media/plays/{play_slug}/photos'
    play_videos_dir = Path(working_dirs[working_env]) / f'media/plays/{play_slug}/videos'
    play_media = defaultdict(dict)
    play_photos = [f for f in os.listdir(play_photos_dir) if os.path.isfile(f'{play_photos_dir}/{f}')]
    play_videos = [
        f for f in os.listdir(play_videos_dir)
        if os.path.isfile(f'{play_videos_dir}/{f}')
        and not f.endswith('mp4')
    ]

    for img in sorted(play_photos, key=lambda x: int(x.split('.')[0])):
        img_file = f'{play_photos_dir}/{img}'
        img_format = get_image_size(img_file)
        width, height = img_format.get_dimensions()
        play_media['photos'][img] = {'width': width, 'height': height}

    for video_file in play_videos:
        play_media['videos'][video_file.split('.')[0]] = video_file

    play_media['details']['total_images'] = len(play_photos)
    play_media['details']['total_videos'] = len(play_videos)

    return play_media


@router.get('/history')
async def fetch_images():
    history_cwd = Path(working_dirs[working_env]) / 'media/history'
    img_files = [f for f in os.listdir(history_cwd) if os.path.isfile(f'{history_cwd}/{f}')]
    history_images = defaultdict(tuple)

    for img in img_files:
        img_file = f'{history_cwd}/{img}'
        img_format = get_image_size(img_file)
        width, height = img_format.get_dimensions()
        history_images[img[:-4]] = img, width, height

    return history_images


@router.get('/stages')
async def fetch_images():
    stages = ['main', 'small', 'children']
    stages_images_dir = Path(working_dirs[working_env]) / f'media/stages'
    stages_dict = defaultdict(list)

    for stage in stages:
        for img in os.listdir(Path(stages_images_dir) / stage / 'photos'):
            img_file = f'{stages_images_dir}/{stage}/photos/{img}'
            if os.path.isfile(img_file):
                img_format = get_image_size(img_file)
                width, height = img_format.get_dimensions()
                stages_dict[stage].append((img, width, height))

        layout_images = ['plan.jpg', 'layout.svg']
        for img in layout_images:
            img_file = f'{stages_images_dir}/{stage}/{img}'
            if os.path.isfile(img_file) and not img_file.endswith('.svg'):
                img_format = get_image_size(img_file)
                width, height = img_format.get_dimensions()
                stages_dict[f'{stage}_plan'] = [img, width, height]

    return stages_dict
