class FoodRatings {
    unordered_map<string,string>foodtocuisine;
    unordered_map<string,int>foodrating;
    unordered_map<string,set<pair<int,string>>>cuisinetofood;
public:
     

    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i =0 ; i <foods.size();i++){
            foodtocuisine[foods[i]] = cuisines[i];
            foodrating[foods[i]] = ratings[i];
            cuisinetofood[cuisines[i]].insert({-ratings[i],foods[i]});
        }
    }
    
    void changeRating(string food, int newRating) {
        string cuisine = foodtocuisine[food];
        int old = foodrating[food];
        cuisinetofood[cuisine].erase({-old,food});
        cuisinetofood[cuisine].insert({-newRating,food});

        foodrating[food]= newRating;


    }
    
    string highestRated(string cuisine) {
        return cuisinetofood[cuisine].begin()->second;
     }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */