#import "ObjCHello.h"

@implementation ObjCHello
- (void)helloToName:(NSString *)name
{
    NSLog(@"Hello %@ from ObjC!", name);
}

- (NSInteger)answerToLife
{
    return 42;
}
@end
