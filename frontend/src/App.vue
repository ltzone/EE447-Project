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
        class="justify-space-between align-center"
      >
        <v-btn fab dark
          to="/" class="mt-4 mx-5"
          color="blue darken-1" small elevation="1"
          ><v-icon dark> mdi-account-circle </v-icon>
        </v-btn>

        <v-divider class="mx-3 my-5"></v-divider>

        <v-btn fab dark
          to="/task" class="my-2 mx-6"
          color="purple lighten-1" x-small elevation="1"
          ><v-icon dark> mdi-file-tree </v-icon>
        </v-btn>

        <v-btn fab dark
          to="/log" class="my-2 mx-6"
          color="yellow lighten-1" x-small elevation="1"
          ><v-icon dark> mdi-alert-decagram </v-icon>
        </v-btn>

        <v-btn fab dark
          to="/stat" class="my-2 mx-6"
          color="green lighten-1" x-small elevation="1"
          ><v-icon dark> mdi-equalizer </v-icon>
        </v-btn>

        <v-btn fab dark
          to="/app" class="my-2 mx-6"
          color="blue lighten-1" x-small elevation="1"
          ><v-icon dark> mdi-application </v-icon>
        </v-btn>

        <v-btn fab dark
          to="/monitor" class="my-2 mx-6"
          color="red lighten-1" x-small elevation="1"
          ><v-icon dark> mdi-eye </v-icon>
        </v-btn>

        <v-btn fab dark
          to="/about" class="my-2 mx-6"
          color="grey lighten-1" x-small elevation="1"
          ><v-icon> mdi-information </v-icon>
        </v-btn>
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
      <router-view/>
      <!--  -->
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({ drawer: null }),
};
</script>



<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
