<script setup lang="ts">
import PhotoSwipeLightbox from "photoswipe/lightbox";
import "photoswipe/style.css";

const props = defineProps<{
  slug?: string;
}>();

const { data: play, error } = await useFetch(setApiUrl(`/images/play-photos/${props.slug}`));
const mainGallery = ref(null);
const navGallery = ref(null);
const displaySize = useState("displaySize");

const lightbox = new PhotoSwipeLightbox({
  gallery: "#mainGallery",
  children: "a",
  pswpModule: () => import("photoswipe"),
});

onMounted(() => {
  if (process.client && mainGallery.value) {
    lightbox.init();
  }
});

onUnmounted(() => {
  lightbox.destroy();
});
</script>

<template lang="html">
  <!-- Title should be set according to play name. Something like {{ _('Picture from') + play.name }} or
      playTranslation.name when the translations are done -->
  <div v-if="play">
    <div ref="mainGallery" id="mainGallery" class="pspw-gallery mt-3 mb-2 ps-3 pe-3">
      <Swiper
        :modules="[SwiperThumbs]"
        slidesPerView="auto"
        class="main-gallery"
        :thumbs="{
          swiper: '.nav-gallery',
          autoScrollOffset: 3,
          multipleActiveThumbs: false,
        }"
      >
        <SwiperSlide v-for="(dimensions, img) in play.play_photos" :key="img">
          <a
            :href="`/media/plays/${slug}/photos/${img}`"
            class="m-2 gallery-slide"
            :data-pswp-width="`${dimensions.width}`"
            :data-pswp-height="`${dimensions.height}`"
            title=""
          >
            <!-- <img
              :src="`/media/plays/${slug}/photos/thumbs/${img}`"
              :alt="`Photo - ${img}`"
              :style="{ width: `${40 * (dimensions.width / dimensions.height)}vh`, height: '40vh' }"
              class="carousel-image"
              loading="lazy"
            /> -->
            <NuxtImg
              format="webp"
              :src="`/media/plays/${slug}/photos/${img}`"
              :alt="`Photo - ${img}`"
              :style="{ width: `${40 * (dimensions.width / dimensions.height)}vh`, height: '40vh' }"
              sizes="300px md:400px lg:300px xl:20vw"
              placeholder
              loading="lazy"
            />
          </a>
          <div class="swiper-lazy-preloader"></div>
        </SwiperSlide>
      </Swiper>
    </div>

    <div ref="navGallery" id="navGallery" class="container mb-3 ps-3 pe-3">
      <Swiper
        :modules="[SwiperThumbs]"
        slidesPerView="auto"
        :centeredSlidesBounds="true"
        :centerInsufficientSlides="true"
        :grabCursor="false"
        class="nav-gallery"
      >
        <SwiperSlide v-for="(dimensions, img) in play.play_photos" :key="img" class="m-1 nav-slide">
          <!-- <img
            :src="`/media/plays/${slug}/photos/thumbs/${img}`"
            :alt="`Thumb - ${img}`"
            :style="{ width: `${100 * (dimensions.width / dimensions.height)}px`, height: '100px' }"
            loading="lazy"
          /> -->
          <NuxtImg
            format="webp"
            :src="`/media/plays/${slug}/photos/${img}`"
            :alt="`Thumb - ${img}`"
            :style="{ width: `${100 * (dimensions.width / dimensions.height)}px`, height: '100px' }"
            sizes="100px"
            placeholder
            loading="lazy"
          />
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style lang="css" scoped>
.swiper-wrapper {
  /* max-width: max-content; */
  /* padding: 50px; */
}

.swiper-slide {
  max-width: max-content;
  /* cursor: pointer; */
}
</style>
