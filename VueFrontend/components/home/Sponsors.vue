<script setup lang="ts">
const { data: sponsorLogos } = useNuxtData("sponsorLogos");
const displaySize = useState("displaySize");

onMounted(() => {
  // if (error.value) {
  //   console.error("Failed to fetch play data:", error.value);
  // }
});
</script>

<template lang="html">
  <div id="sponsorsContainer" class="d-flex justify-content-center">
    <!-- <img
      v-if="['xs', 'sm'].includes(displaySize)"
      :src="setThumborUrl('/dkts_background_1.jpg', 'unsafe/450x0/filters:format(webp)')"
      id="backgroundImgMobile"
      class="img-fluid d-block d-md-none background-img"
      alt=""
    />
    <img
      v-if="['md'].includes(displaySize)"
      :src="setThumborUrl('/dkts_background_1.jpg', 'unsafe/810x0/filters:format(webp)')"
      id="backgroundImgMobile"
      class="img-fluid d-none d-md-block d- background-img"
      alt=""
    />
    <img
      v-if="['lg'].includes(displaySize)"
      :src="setThumborUrl('/dkts_background_1.jpg', 'unsafe/1080x0/filters:format(webp)')"
      id="backgroundImgMobile"
      class="img-fluid d-none d-md-block d- background-img"
      alt=""
    />
    <img
      v-if="['xl', 'xxl'].includes(displaySize)"
      :src="setThumborUrl('/dkts_background_1.jpg', 'unsafe/1920x0/filters:format(webp)')"
      id="backgroundImgDesktop"
      class="img-fluid d-none d-xl-block background-img"
      alt=""
    /> -->
    <NuxtImg
      format="webp"
      src="/dkts_background_1.jpg"
      id="sponsorsBackgrnd"
      class="img-fluid background-img"
      alt="sponsorsBackgroundImage"
      width="4167"
      height="833"
      sizes="100vw md:810px lg:50vw"
      placeholder
    />
    <div id="sponsorsCarousel" class="container d-flex align-items-center text-center">
      <Swiper
        :modules="[SwiperAutoplay, SwiperPagination]"
        slidesPerView="auto"
        :centeredSlides="true"
        :centeredSlidesBounds="true"
        spaceBetween="40"
        :autoplay="{
          delay: 3500,
          disableOnInteraction: true,
        }"
      >
        <SwiperSlide v-for="(sizes, img) in sponsorLogos" :key="`desktop-${img}`">
          <!-- <img :src="`/sponsors/${img}`" :alt="img" class="img-fluid sponsor-logo" /> -->
          <NuxtImg
            format="webp"
            :src="`/sponsors/${img}`"
            :alt="img"
            class="img-fluid sponsor-logo ms-0 me-0 ps-2 pe-2"
          />
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style lang="css" scoped>
#sponsorsContainer {
  height: 200px;
  position: relative;
}

#sponsorsContainer .background-img {
  width: 100%;
  height: 100%;
  position: absolute;
  object-fit: cover;
  z-index: -9999;
}

#sponsorsCarousel {
  /* max-width: 550px; */
}

.sponsor-logo {
  max-height: 100px;
  /* margin: 20px; */
  /* margin-top: 50px; */
}

.swiper-slide {
  align-self: center;
  max-width: max-content;
}
</style>
