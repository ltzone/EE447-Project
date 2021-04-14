<template>
  <v-app id="inspire">
    <v-system-bar app>
      Your Distributed System
      <v-spacer></v-spacer>

      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>

      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-app-bar app clipped-right flat height="72">
      <v-spacer></v-spacer>

      <v-responsive max-width="156">
        <v-text-field
          dense
          flat
          hide-details
          rounded
          solo-inverted
        ></v-text-field>
      </v-responsive>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app width="300">
      <v-navigation-drawer
        v-model="drawer"
        absolute
        color="grey lighten-3"
        mini-variant
      >
        <v-avatar
          class="d-block text-center mx-auto mt-4"
          color="blue darken-1"
          size="36"
        >
          <v-icon dark> mdi-account-circle </v-icon>
        </v-avatar>

        <v-divider class="mx-3 my-5"></v-divider>

        <v-avatar
          class="d-block text-center mx-auto mb-9"
          color="yellow darken-3"
          size="28"
          ><v-icon dark> mdi-alert-decagram </v-icon>
        </v-avatar>

        <v-avatar
          class="d-block text-center mx-auto mb-9"
          color="purple lighten-1"
          size="28"
          ><v-icon dark> mdi-file-tree </v-icon>
        </v-avatar>

        <v-avatar
          class="d-block text-center mx-auto mb-9"
          color="green lighten-1"
          size="28"
          ><v-icon dark> mdi-equalizer </v-icon>
        </v-avatar>

        <v-avatar
          class="d-block text-center mx-auto mb-9"
          color="blue lighten-1"
          size="28"
          ><v-icon dark> mdi-application </v-icon>
        </v-avatar>

        <v-avatar
          class="d-block text-center mx-auto mb-9"
          color="red lighten-1"
          size="28"
          ><v-icon dark> mdi-eye </v-icon>
        </v-avatar>
      </v-navigation-drawer>

      <v-sheet color="grey lighten-5" height="128" width="100%">
      </v-sheet>

      <v-list class="pl-14" shaped>
        <v-list-item v-for="n in 5" :key="n" link>
          <v-list-item-content>
            <v-list-item-title>Cluster {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-navigation-drawer app clipped right>
      <v-list>
        <v-list-item v-for="n in 5" :key="n" link>
          <v-list-item-content>
            <v-list-item-title>Item {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <!--  -->
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({ drawer: null }),
};
</script>