<script setup lang="ts">
const head = useLocaleHead({
  identifierAttribute: "id",
  addSeoAttributes: true,
});
</script>

<template lang="html">
  <div class="d-flex flex-column min-vh-100">
    <Html :lang="head.htmlAttrs.lang" :dir="head.htmlAttrs.dir">
      <Head>
        <template v-for="link in head.link" :key="link.id">
          <Link :id="link.id" :rel="link.rel" :href="link.href" :hreflang="link.hreflang" />
        </template>
        <template v-for="meta in head.meta" :key="meta.id">
          <Meta :id="meta.id" :property="meta.property" :content="meta.content" />
        </template>
      </Head>
      <AppHeader />
      <div>
        <Body>
          <slot />
        </Body>
      </div>
      <AppFooter />
    </Html>
  </div>
</template>

<style lang="css" scoped></style>
