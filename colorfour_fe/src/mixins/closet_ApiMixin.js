import axios from "axios";

export const closetApiMixin = {
  methods: {
    async fetchItems(endpoint) {
      try {
        const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${endpoint}/`, {
          headers: {
            Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
          },
        });
        console.log("Items fetched successfully:", response.data);
        this.items = response.data;
        this.extractBrands();
      } catch (error) {
        console.error("Error fetching items:", error);
      }
    },

    async modifyItem(action, itemIds) {
      try {
        if (!Array.isArray(itemIds)) {
          itemIds = [itemIds]; // Wrap single item in an array
        }

        await Promise.all(
          itemIds.map(async (id) => {
            let endpoint = `${id}/`;
            let requestMethod = axios.post;

            if (action === "restore") {
              endpoint += "restore/";
            } else if (action === "delete") {
              requestMethod = axios.delete;
              endpoint += "permanent_delete/";
            } else if (action === "move_to_trash") {
              endpoint += "move_to_trash/";
            } else if (action === "add_to_favorites") {
              endpoint += "add_to_favorites/";
            } else if (action === "remove_from_favorites") {
              endpoint += "remove_from_favorites/";
            }

            // Send the request
            await requestMethod(
              `${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${endpoint}`,
              {}, // No payload needed for DELETE
              {
                headers: {
                  Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
                },
              }
            );
          })
        );

        console.log(`Items successfully ${action === "restore" ? "restored" : "deleted"}.`);
      } catch (error) {
        console.error(`Error performing ${action} on items:`, error);
      }
    },
  },
};
