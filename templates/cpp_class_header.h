#ifndef __NAMEclass__
#define __NAMEclass__

class NAME {
public:
    // interface
    // ------
    NAME();
    ~NAME();
    NAME(const NAME &other);
    NAME& operator=(const NAME &other);

       
private:
    // members
    // ------
    
    // methods
    void to_string() const;

};

#endif