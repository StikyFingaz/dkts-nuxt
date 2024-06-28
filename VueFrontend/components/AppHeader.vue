<script setup lang="ts">
const nuxtApp = useNuxtApp();
const localePath = useLocalePath();
const userLocale = useState("userLocale");
const { data: translations } = useNuxtData("commonStrings");

const offcanvasNavbar = ref(null);
const showOffcanvasHandler = ref(null);
const hideOffcanvasHandler = ref(null);

const togglerState = ref(true);
const closeOffcanvasNavbar = () => {
  offcanvasNavbar.value.hide();
};

onMounted(async () => {
  if (process.client) {
    const { Offcanvas } = nuxtApp.$bootstrap;

    offcanvasNavbar.value = new Offcanvas("#offcanvasNavbar");

    showOffcanvasHandler.value = (event) => {
      togglerState.value = false;
    };

    hideOffcanvasHandler.value = (event) => {
      togglerState.value = true;
    };
    offcanvasNavbar.value._element.addEventListener("show.bs.offcanvas", showOffcanvasHandler.value);
    offcanvasNavbar.value._element.addEventListener("hide.bs.offcanvas", hideOffcanvasHandler.value);
  }
});

onBeforeUnmount(() => {
  offcanvasNavbar.value._element.removeEventListener("show.bs.offcanvas", showOffcanvasHandler.value);
  offcanvasNavbar.value._element.removeEventListener("hide.bs.offcanvas", hideOffcanvasHandler.value);
});
</script>

<template lang="html">
  <nav id="navbar" class="navbar navbar-expand-lg bg-dark shadow sticky-top" data-bs-theme="dark">
    <div class="container">
      <NuxtLink class="navbar-brand" :to="localePath('/')" @click="closeOffcanvasNavbar">
        <img src="/logo-website_top.svg" alt="DKTS Logo" height="40" />
      </NuxtLink>
      <HeaderToggler :togglerState="togglerState" />
      <div
        id="offcanvasNavbar"
        class="offcanvas offcanvas-start text-bg-dark"
        tabindex="-1"
        data-bs-backdrop="false"
        aria-labelledby="offcanvasNavbarLabel"
      >
        <div class="offcanvas-header text-bg-dark">
          <div id="mobileSearch" class="d-block d-lg-none">
            <HeaderSearchBar :placeholder="translations.search" @closeMenu="closeOffcanvasNavbar" />
          </div>
        </div>
        <div class="offcanvas-body">
          <!-- Lefthand items -->
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <NuxtLink class="nav-link link-light ms-3 ms-lg-0" :to="localePath('/')" @click="closeOffcanvasNavbar">
              {{ translations.home }}
            </NuxtLink>
            <NuxtLink
              class="nav-link link-light ms-3 ms-lg-0"
              :to="localePath('/events/plays')"
              @click="closeOffcanvasNavbar"
            >
              {{ translations.repertoire }}
            </NuxtLink>
            <HeaderAboutDropdown class="ms-3 ms-lg-0" :closeMenu="closeOffcanvasNavbar" />
            <HeaderLangDropdown class="ms-3 ms-lg-0" :closeMenu="closeOffcanvasNavbar" />
          </ul>
          <!-- SearchBar -->
          <div id="desktopSearch" class="d-none d-lg-block me-auto">
            <HeaderSearchBar :placeholder="translations.search" />
          </div>
          <!-- Righthand items -->
          <ul class="navbar-nav d-flex">
            <li class="nav-item">
              <a
                class="nav-link link-light ms-3 ms-lg-0"
                href="https://www.entase.bg/dktshumen"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span class="d-flex align-items-center">
                  {{ translations.tickets }}
                  <Icon class="ms-2" name="bi:arrow-up-right-square" />
                </span>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link link-light badge text-bg-danger"
                :href="`https://www.entase.com/dktshumen/?lc=${userLocale}`"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span class="d-flex align-items-center ms-3 me-3">
                  {{ translations.tk_festival }}
                  <Icon class="ms-2" name="bi:arrow-up-right-square" />
                </span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="css">
#navbar {
  /* background-color: #960014 !important; */
}

#offcanvasNavbar {
  top: 65px;
}

#mobileSearch {
  width: 75%;
}

#desktopSearch {
  width: 25%;
}
</style>
