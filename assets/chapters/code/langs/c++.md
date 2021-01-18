# C++


 * C++11 INHERITANCE

 ```c++
class GameObject
{
    public:
        virtual ~GameObject() {}
        virtual void update() {}
        virtual void draw() {}
        virtual void collide(Object objects[]) {}
};

class Visible : public GameObject
{
    public:
        virtual void draw() override { /* draw model at position of this object */ };
    private:
        Model* model;
};

class Solid : public GameObject
{
    public:
        virtual void collide(GameObject objects[]) override { /* check and react to collisions with objects */ };
};

class Movable : public GameObject
{
    public:
        virtual void update() override { /* update position */ };
};
 ```
