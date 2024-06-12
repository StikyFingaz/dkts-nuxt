<script setup lang="ts">
const { data: images } = useNuxtData("carouselImages");
const displaySize = useState("displaySize");
</script>

<template lang="html">
  <div id="desktopCarousel" class="container border border-0 mt-3">
    <Swiper
      :modules="[SwiperAutoplay, SwiperEffectCoverflow, SwiperPagination]"
      :effect="'coverflow'"
      :autoplay="{
        delay: 3500,
        disableOnInteraction: true,
      }"
      :pagination="{
        enabled: true,
        type: 'bullets',
      }"
    >
      <SwiperSlide v-for="img in images.desktopImages" :key="`desktop-${img}`">
        <NuxtLinkLocale :to="`/events/plays/${img.split('.')[0]}`">
          <!-- <img
            v-if="['md', 'lg'].includes(displaySize)"
            :src="setThumborUrl(`/media/main-carousel/${img}`, 'unsafe/850x0/filters:format(webp)')"
            class="img-fluid col-12"
            alt=""
            width="850"
            height="445"
            loading="lazy"
          />
          <img
            v-if="['xl', 'xxl'].includes(displaySize)"
            :src="setThumborUrl(`/media/main-carousel/${img}`, 'unsafe/1050x0/filters:format(webp)')"
            class="img-fluid col-12"
            alt=""
            width="1050"
            height="550"
            loading="lazy"
          /> -->
          <NuxtImg
            format="webp"
            :src="`/media/main-carousel/mobile/${img}`"
            :alt="`Poster: ${img}`"
            class="d-block d-md-none img-fluid col-12"
            width="10"
            height="14"
            sizes="350px"
            loading="lazy"
          />
          <NuxtImg
            format="webp"
            :src="`/media/main-carousel/${img}`"
            :alt="`Poster: ${img}`"
            class="d-none d-md-block img-fluid col-12"
            width="1920"
            height="1005"
            sizes="90vw lg:840px xl:1040px"
            loading="lazy"
          />
        </NuxtLinkLocale>
        <div class="swiper-lazy-preloader"></div>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style lang="css" scoped>
#desktopCarousel {
  max-width: calc(100vh + 100px);
}

.swiper {
  --swiper-pagination-color: whitesmoke;
  /* --swiper-pagination-bottom: 0px; */
}
</style>
