trait GeorgeFloyd
trait Leg

class Policeman extends GeorgeFloyd with Leg

object Main extends App {
    val l = List(1, 2, 3, 4)
    .map(_ * 2)
    .takeWhile(_ < 5)
    println(l)
}