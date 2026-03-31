# MoroAcademy Learning Journeys

User journey maps and UX patterns for trainees and students on the MoroAcademy learning platform.

## Table of Contents
- [Overview](#overview)
- [Discovery & Enrollment Journey](#discovery--enrollment-journey)
- [Learning Journey](#learning-journey)
- [Progress & Achievement Journey](#progress--achievement-journey)
- [Certification Journey](#certification-journey)

## Overview

MoroAcademy is the training and capacity-building platform within the Negosyo ecosystem, aligned with BDP 2023-2028 Goal 4 (Inclusive, Responsive, and Quality Social Services) and the education sector strategies.

### Training Areas
- **Cooperative Management Training** - Governance, finance, operations
- **Business Skills** - Marketing, product development, e-commerce
- **Compliance Training** - FRAMES requirements, regulatory updates
- **Technical Skills** - Digital literacy, platform usage
- **Livelihood Skills** - TVET-aligned programs for employability
- **Madaris Integration** - Business skills for Islamic education graduates

---

## BARMM Education Context (BDP 2023-2028)

### Education Challenges in BARMM
Understanding learner context is critical for MoroAcademy UX design:

| Indicator | BARMM | National Average | Notes |
|-----------|-------|------------------|-------|
| Functional Literacy Rate | 71.6% | 91.6% | Lowest among regions |
| Dropout Rate (Grades 1-7) | 8.36% | 3.76% | Highest among regions |
| Completion Rate (Grades 1-6) | 63.98% | 82.51% | Lowest among regions |
| Completion Rate (Grades 7-12) | 56.89% | 69.32% | 3rd lowest |

### Contributing Factors
- High poverty incidence - children help with family income instead of schooling
- Armed conflict history causing displacement and uncertainty
- Teacher shortages in Grades 1-3 and 4-12 (actual ratio exceeds standard)
- 104 unserved/underserved barangays for basic education
- Geographically isolated and disadvantaged areas (GIDA)

### TVET Context
- 25,002 TVET graduates (2021), but only 60% completed competency assessment
- 94% certification rate among those assessed
- Limited assessment centers across region
- Strong demand for construction, tourism, electrical/electronics sectors

### Madaris Education
- 1,679 madrasah in BARMM, only 117 (7%) accredited
- 4,868 Asatidz (Arabic teachers) deployed to public schools
- Need for business skills integration with Islamic education

### Priority Strategies (BDP 2023-2028)
1. Ensure inclusive, equitable access through universal early childhood education
2. Provide quality, relevant, and responsive education considering industrial demands
3. Strengthen education management through digitalization
4. Systematic institutionalization of Madaris education

---

## User Personas

| Persona | Description | Goals | BARMM Context |
|---------|-------------|-------|---------------|
| **New Coop Member** | Recently joined cooperative | Learn basics of cooperative principles | May have limited formal education; needs mobile-friendly, visual content |
| **Aspiring Manager** | Wants to lead their cooperative | Gain management and leadership skills | May be from rural area; needs offline access capability |
| **Compliance Officer** | Handles FRAMES regulatory requirements | Stay updated on FRAMES compliance | Coordinates with CSEA; needs practical, compliance-focused modules |
| **Digital Novice** | Limited tech experience | Learn to use Negosyo platform | 71.6% functional literacy rate context; needs simplified UX |
| **Out-of-School Youth (OSY)** | Youth seeking livelihood skills | Gain employable skills, TVET certification | 1 in 10 reach college; needs pathways to certification |
| **Madrasah Graduate** | Completed Islamic education | Add business/cooperative skills to religious education | Bridge Madaris and modern business skills |
| **IDP Learner** | Internally displaced person | Rebuild livelihood capabilities | 93,525 IDPs in BARMM; needs accessible, trauma-informed content |
| **Women Entrepreneur** | Member of women's organization | Build business and leadership skills | Part of women empowerment programs (WECoRe, Women Livelihood Acceleration) |
| **Asatidz (Arabic Teacher)** | Islamic educator in public school | Complement teaching with cooperative/business knowledge | Part of 4,868 deployed Asatidz |
| **PWD Learner** | Person with disability | Access inclusive training opportunities | 53,483 PWDs with capacity needs; requires WCAG-compliant design |

---

## Discovery & Enrollment Journey

### Course Catalog

```tsx
// MoroAcademy Course Catalog
<div className="space-y-6">
  {/* Hero Section */}
  <div className="bg-gradient-to-r from-negosyo-blue to-negosyo-blue/80 text-white rounded-lg p-8">
    <h1 className="text-3xl font-bold">MoroAcademy</h1>
    <p className="mt-2 text-white/90 max-w-2xl">
      Build the skills you need to succeed. Free training for cooperatives
      and social enterprises in the Bangsamoro region.
    </p>
    <div className="mt-6 flex gap-4">
      <Button variant="secondary" size="lg">
        Browse Courses
      </Button>
      <Button variant="outline" size="lg" className="text-white border-white hover:bg-white/10">
        My Learning
      </Button>
    </div>
  </div>

  {/* Categories */}
  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
    {categories.map((category) => (
      <Card
        key={category.id}
        className="cursor-pointer hover:border-primary transition-colors"
        onClick={() => filterByCategory(category.id)}
      >
        <CardContent className="p-4 text-center">
          <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-3">
            <category.icon className="h-6 w-6 text-primary" />
          </div>
          <p className="font-medium">{category.name}</p>
          <p className="text-sm text-muted-foreground">{category.courseCount} courses</p>
        </CardContent>
      </Card>
    ))}
  </div>

  {/* Course Grid */}
  <div>
    <div className="flex items-center justify-between mb-4">
      <h2 className="text-xl font-semibold">Popular Courses</h2>
      <Select defaultValue="popular">
        <SelectTrigger className="w-40">
          <SelectValue />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="popular">Most Popular</SelectItem>
          <SelectItem value="newest">Newest</SelectItem>
          <SelectItem value="rating">Highest Rated</SelectItem>
        </SelectContent>
      </Select>
    </div>

    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  </div>
</div>
```

### Course Card Component

```tsx
// Course Card
function CourseCard({ course }: { course: Course }) {
  return (
    <Card className="overflow-hidden group">
      {/* Thumbnail */}
      <div className="relative aspect-video">
        <Image
          src={course.thumbnail}
          alt={course.title}
          fill
          className="object-cover group-hover:scale-105 transition-transform"
        />
        {course.isFree && (
          <Badge className="absolute top-2 left-2 bg-green-600">
            Free
          </Badge>
        )}
        <div className="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">
          {course.duration}
        </div>
      </div>

      <CardContent className="p-4">
        {/* Category */}
        <Badge variant="outline" className="mb-2">
          {course.category}
        </Badge>

        {/* Title */}
        <h3 className="font-semibold line-clamp-2 group-hover:text-primary transition-colors">
          {course.title}
        </h3>

        {/* Instructor */}
        <p className="text-sm text-muted-foreground mt-1">
          {course.instructor}
        </p>

        {/* Stats */}
        <div className="flex items-center gap-4 mt-3 text-sm">
          <div className="flex items-center gap-1">
            <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
            <span className="font-medium">{course.rating}</span>
          </div>
          <span className="text-muted-foreground">
            {course.enrolledCount.toLocaleString()} enrolled
          </span>
        </div>

        {/* Progress (if enrolled) */}
        {course.progress !== undefined && (
          <div className="mt-3 space-y-1">
            <div className="flex justify-between text-xs">
              <span className="text-muted-foreground">Progress</span>
              <span className="font-medium">{course.progress}%</span>
            </div>
            <Progress value={course.progress} className="h-1.5" />
          </div>
        )}
      </CardContent>

      <CardFooter className="p-4 pt-0">
        {course.progress !== undefined ? (
          <Button className="w-full" asChild>
            <Link href={`/moro-academy/courses/${course.id}/learn`}>
              Continue Learning
            </Link>
          </Button>
        ) : (
          <Button className="w-full" variant="outline" asChild>
            <Link href={`/moro-academy/courses/${course.id}`}>
              View Course
            </Link>
          </Button>
        )}
      </CardFooter>
    </Card>
  );
}
```

### Course Detail & Enrollment

```tsx
// Course Detail Page
<div className="container py-8">
  {/* Breadcrumb */}
  <Breadcrumb items={[
    { label: 'MoroAcademy', href: '/moro-academy' },
    { label: course.category, href: `/moro-academy?category=${course.categoryId}` },
    { label: course.title },
  ]} />

  <div className="grid lg:grid-cols-3 gap-8 mt-6">
    {/* Main Content */}
    <div className="lg:col-span-2 space-y-6">
      {/* Video Preview */}
      <div className="relative aspect-video rounded-lg overflow-hidden bg-black">
        <Image src={course.thumbnail} alt="" fill className="object-cover" />
        <button
          className="absolute inset-0 flex items-center justify-center bg-black/40 hover:bg-black/50 transition-colors"
          onClick={playPreview}
        >
          <div className="h-16 w-16 rounded-full bg-white/90 flex items-center justify-center">
            <Play className="h-8 w-8 text-primary ml-1" />
          </div>
        </button>
      </div>

      {/* Course Info */}
      <div>
        <Badge variant="outline">{course.category}</Badge>
        <h1 className="text-2xl font-bold mt-2">{course.title}</h1>
        <p className="text-muted-foreground mt-2">{course.description}</p>

        {/* Meta */}
        <div className="flex flex-wrap gap-4 mt-4 text-sm">
          <div className="flex items-center gap-1">
            <Star className="h-4 w-4 fill-yellow-400 text-yellow-400" />
            <span className="font-medium">{course.rating}</span>
            <span className="text-muted-foreground">({course.reviewCount} reviews)</span>
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            <Users className="h-4 w-4" />
            {course.enrolledCount.toLocaleString()} enrolled
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            <Clock className="h-4 w-4" />
            {course.duration}
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            <FileText className="h-4 w-4" />
            {course.lessonCount} lessons
          </div>
        </div>

        {/* Instructor */}
        <div className="flex items-center gap-3 mt-6 p-4 bg-muted rounded-lg">
          <Avatar className="h-12 w-12">
            <AvatarImage src={course.instructor.avatar} />
            <AvatarFallback>{course.instructor.initials}</AvatarFallback>
          </Avatar>
          <div>
            <p className="font-medium">{course.instructor.name}</p>
            <p className="text-sm text-muted-foreground">{course.instructor.title}</p>
          </div>
        </div>
      </div>

      {/* Curriculum */}
      <Card>
        <CardHeader>
          <CardTitle>Course Curriculum</CardTitle>
        </CardHeader>
        <CardContent>
          <Accordion type="multiple" className="w-full">
            {course.modules.map((module, i) => (
              <AccordionItem key={module.id} value={module.id}>
                <AccordionTrigger className="hover:no-underline">
                  <div className="flex items-center gap-3">
                    <span className="h-6 w-6 rounded-full bg-primary/10 text-primary text-xs flex items-center justify-center">
                      {i + 1}
                    </span>
                    <span>{module.title}</span>
                    <Badge variant="secondary" className="ml-auto mr-2">
                      {module.lessons.length} lessons
                    </Badge>
                  </div>
                </AccordionTrigger>
                <AccordionContent>
                  <div className="space-y-2 pl-9">
                    {module.lessons.map((lesson) => (
                      <div
                        key={lesson.id}
                        className="flex items-center justify-between py-2 text-sm"
                      >
                        <div className="flex items-center gap-2">
                          {lesson.type === 'video' ? (
                            <PlayCircle className="h-4 w-4 text-muted-foreground" />
                          ) : lesson.type === 'quiz' ? (
                            <HelpCircle className="h-4 w-4 text-muted-foreground" />
                          ) : (
                            <FileText className="h-4 w-4 text-muted-foreground" />
                          )}
                          <span>{lesson.title}</span>
                        </div>
                        <span className="text-muted-foreground">{lesson.duration}</span>
                      </div>
                    ))}
                  </div>
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </CardContent>
      </Card>
    </div>

    {/* Sidebar - Enrollment Card */}
    <div>
      <Card className="sticky top-4">
        <CardContent className="p-6">
          {course.isFree ? (
            <div className="text-center mb-4">
              <Badge className="bg-green-600 text-lg px-4 py-1">
                Free Course
              </Badge>
            </div>
          ) : (
            <p className="text-3xl font-bold text-center mb-4">
              PHP {course.price.toLocaleString()}
            </p>
          )}

          <Button className="w-full" size="lg">
            {course.isEnrolled ? 'Continue Learning' : 'Enroll Now'}
          </Button>

          {/* What You'll Learn */}
          <div className="mt-6">
            <p className="font-medium mb-3">What you'll learn:</p>
            <ul className="space-y-2">
              {course.learningOutcomes.map((outcome, i) => (
                <li key={i} className="flex gap-2 text-sm">
                  <CheckCircle className="h-4 w-4 text-green-600 shrink-0 mt-0.5" />
                  <span>{outcome}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Requirements */}
          <div className="mt-6">
            <p className="font-medium mb-3">Requirements:</p>
            <ul className="space-y-2">
              {course.requirements.map((req, i) => (
                <li key={i} className="flex gap-2 text-sm text-muted-foreground">
                  <span>•</span>
                  <span>{req}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Certificate */}
          {course.hasCertificate && (
            <div className="mt-6 p-4 bg-muted rounded-lg flex items-center gap-3">
              <Award className="h-8 w-8 text-primary" />
              <div>
                <p className="font-medium text-sm">Certificate of Completion</p>
                <p className="text-xs text-muted-foreground">
                  Earn a certificate upon finishing this course
                </p>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  </div>
</div>
```

---

## Learning Journey

### Course Player Interface

```tsx
// Learning Player
<div className="min-h-screen bg-background">
  {/* Top Bar */}
  <header className="sticky top-0 z-50 border-b bg-background">
    <div className="flex items-center justify-between h-14 px-4">
      <div className="flex items-center gap-4">
        <Button variant="ghost" size="icon" asChild>
          <Link href={`/moro-academy/courses/${courseId}`}>
            <X className="h-5 w-5" />
          </Link>
        </Button>
        <div className="hidden md:block">
          <p className="font-medium line-clamp-1">{course.title}</p>
          <p className="text-xs text-muted-foreground">{currentLesson.title}</p>
        </div>
      </div>

      {/* Progress */}
      <div className="flex items-center gap-4">
        <div className="hidden sm:flex items-center gap-2">
          <Progress value={progress} className="w-32 h-2" />
          <span className="text-sm text-muted-foreground">{progress}%</span>
        </div>
        <Button variant="outline" size="sm">
          <HelpCircle className="h-4 w-4 mr-2" />
          Help
        </Button>
      </div>
    </div>
  </header>

  <div className="flex">
    {/* Sidebar - Lessons */}
    <aside className="hidden lg:block w-80 border-r h-[calc(100vh-56px)] overflow-y-auto">
      <div className="p-4">
        <h3 className="font-semibold mb-4">Course Content</h3>
        <Accordion type="multiple" defaultValue={[currentModule.id]}>
          {course.modules.map((module) => (
            <AccordionItem key={module.id} value={module.id}>
              <AccordionTrigger className="text-sm hover:no-underline">
                {module.title}
              </AccordionTrigger>
              <AccordionContent>
                <div className="space-y-1">
                  {module.lessons.map((lesson) => (
                    <button
                      key={lesson.id}
                      onClick={() => goToLesson(lesson.id)}
                      className={cn(
                        "w-full flex items-center gap-2 p-2 rounded text-sm text-left hover:bg-muted transition-colors",
                        lesson.id === currentLesson.id && "bg-primary/10 text-primary",
                        lesson.completed && "text-muted-foreground"
                      )}
                    >
                      {lesson.completed ? (
                        <CheckCircle className="h-4 w-4 text-green-600 shrink-0" />
                      ) : lesson.id === currentLesson.id ? (
                        <PlayCircle className="h-4 w-4 shrink-0" />
                      ) : (
                        <Circle className="h-4 w-4 shrink-0" />
                      )}
                      <span className="flex-1 line-clamp-1">{lesson.title}</span>
                      <span className="text-xs text-muted-foreground">{lesson.duration}</span>
                    </button>
                  ))}
                </div>
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </aside>

    {/* Main Content */}
    <main className="flex-1 h-[calc(100vh-56px)] overflow-y-auto">
      {currentLesson.type === 'video' ? (
        <VideoPlayer
          src={currentLesson.videoUrl}
          onComplete={markLessonComplete}
        />
      ) : currentLesson.type === 'quiz' ? (
        <QuizComponent
          questions={currentLesson.questions}
          onComplete={handleQuizComplete}
        />
      ) : (
        <ArticleContent content={currentLesson.content} />
      )}

      {/* Lesson Navigation */}
      <div className="p-4 border-t flex justify-between">
        <Button
          variant="outline"
          onClick={goToPreviousLesson}
          disabled={!previousLesson}
        >
          <ChevronLeft className="h-4 w-4 mr-2" />
          Previous
        </Button>
        <Button onClick={goToNextLesson} disabled={!nextLesson}>
          {nextLesson ? (
            <>
              Next Lesson
              <ChevronRight className="h-4 w-4 ml-2" />
            </>
          ) : (
            <>
              Complete Course
              <Award className="h-4 w-4 ml-2" />
            </>
          )}
        </Button>
      </div>
    </main>
  </div>
</div>
```

### Mobile Learning View

```tsx
// Mobile Course Player
<div className="min-h-screen flex flex-col lg:hidden">
  {/* Video/Content Area */}
  <div className="flex-shrink-0">
    <VideoPlayer src={currentLesson.videoUrl} />
  </div>

  {/* Content Tabs */}
  <Tabs defaultValue="content" className="flex-1 flex flex-col">
    <TabsList className="w-full justify-start border-b rounded-none px-4">
      <TabsTrigger value="content">Lessons</TabsTrigger>
      <TabsTrigger value="notes">Notes</TabsTrigger>
      <TabsTrigger value="resources">Resources</TabsTrigger>
    </TabsList>

    <TabsContent value="content" className="flex-1 overflow-y-auto p-4">
      {/* Lesson List - Simplified for mobile */}
      <div className="space-y-2">
        {allLessons.map((lesson, i) => (
          <button
            key={lesson.id}
            onClick={() => goToLesson(lesson.id)}
            className={cn(
              "w-full flex items-center gap-3 p-3 rounded-lg text-left",
              lesson.id === currentLesson.id
                ? "bg-primary/10 border border-primary"
                : "bg-muted hover:bg-muted/80"
            )}
          >
            <div className={cn(
              "h-8 w-8 rounded-full flex items-center justify-center text-sm",
              lesson.completed && "bg-green-100 text-green-600",
              lesson.id === currentLesson.id && !lesson.completed && "bg-primary text-white",
              !lesson.completed && lesson.id !== currentLesson.id && "bg-muted-foreground/20"
            )}>
              {lesson.completed ? (
                <Check className="h-4 w-4" />
              ) : (
                i + 1
              )}
            </div>
            <div className="flex-1 min-w-0">
              <p className="font-medium text-sm line-clamp-1">{lesson.title}</p>
              <p className="text-xs text-muted-foreground">{lesson.duration}</p>
            </div>
          </button>
        ))}
      </div>
    </TabsContent>

    <TabsContent value="notes" className="flex-1 p-4">
      <Textarea
        placeholder="Take notes here..."
        className="min-h-[200px]"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />
      <Button className="mt-4" size="sm">Save Notes</Button>
    </TabsContent>

    <TabsContent value="resources" className="flex-1 p-4">
      {currentLesson.resources?.map((resource) => (
        <a
          key={resource.id}
          href={resource.url}
          className="flex items-center gap-3 p-3 rounded-lg bg-muted hover:bg-muted/80"
          download
        >
          <FileText className="h-5 w-5 text-muted-foreground" />
          <div className="flex-1">
            <p className="font-medium text-sm">{resource.name}</p>
            <p className="text-xs text-muted-foreground">{resource.type}</p>
          </div>
          <Download className="h-4 w-4 text-muted-foreground" />
        </a>
      ))}
    </TabsContent>
  </Tabs>
</div>
```

---

## Progress & Achievement Journey

### My Learning Dashboard

```tsx
// Learning Dashboard
<div className="container py-8">
  <h1 className="text-2xl font-bold">My Learning</h1>

  {/* Stats */}
  <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
    <Card>
      <CardContent className="p-4 text-center">
        <BookOpen className="h-8 w-8 text-primary mx-auto mb-2" />
        <p className="text-2xl font-bold">{stats.coursesInProgress}</p>
        <p className="text-sm text-muted-foreground">In Progress</p>
      </CardContent>
    </Card>
    <Card>
      <CardContent className="p-4 text-center">
        <CheckCircle className="h-8 w-8 text-green-600 mx-auto mb-2" />
        <p className="text-2xl font-bold">{stats.coursesCompleted}</p>
        <p className="text-sm text-muted-foreground">Completed</p>
      </CardContent>
    </Card>
    <Card>
      <CardContent className="p-4 text-center">
        <Award className="h-8 w-8 text-yellow-600 mx-auto mb-2" />
        <p className="text-2xl font-bold">{stats.certificatesEarned}</p>
        <p className="text-sm text-muted-foreground">Certificates</p>
      </CardContent>
    </Card>
    <Card>
      <CardContent className="p-4 text-center">
        <Clock className="h-8 w-8 text-muted-foreground mx-auto mb-2" />
        <p className="text-2xl font-bold">{stats.hoursLearned}h</p>
        <p className="text-sm text-muted-foreground">Learning Time</p>
      </CardContent>
    </Card>
  </div>

  {/* Continue Learning */}
  <div className="mt-8">
    <h2 className="text-lg font-semibold mb-4">Continue Learning</h2>
    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {inProgressCourses.map((course) => (
        <Card key={course.id}>
          <CardContent className="p-4">
            <div className="flex gap-4">
              <Image
                src={course.thumbnail}
                alt={course.title}
                width={80}
                height={60}
                className="rounded object-cover"
              />
              <div className="flex-1 min-w-0">
                <p className="font-medium line-clamp-2">{course.title}</p>
                <p className="text-sm text-muted-foreground mt-1">
                  {course.completedLessons}/{course.totalLessons} lessons
                </p>
              </div>
            </div>
            <div className="mt-4 space-y-2">
              <div className="flex justify-between text-sm">
                <span className="text-muted-foreground">Progress</span>
                <span className="font-medium">{course.progress}%</span>
              </div>
              <Progress value={course.progress} className="h-2" />
            </div>
            <Button className="w-full mt-4" asChild>
              <Link href={`/moro-academy/courses/${course.id}/learn`}>
                Continue
              </Link>
            </Button>
          </CardContent>
        </Card>
      ))}
    </div>
  </div>

  {/* Completed Courses */}
  <div className="mt-8">
    <h2 className="text-lg font-semibold mb-4">Completed</h2>
    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {completedCourses.map((course) => (
        <Card key={course.id}>
          <CardContent className="p-4">
            <div className="flex gap-4">
              <div className="relative">
                <Image
                  src={course.thumbnail}
                  alt={course.title}
                  width={80}
                  height={60}
                  className="rounded object-cover"
                />
                <div className="absolute -top-1 -right-1 h-6 w-6 rounded-full bg-green-600 flex items-center justify-center">
                  <Check className="h-4 w-4 text-white" />
                </div>
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-medium line-clamp-2">{course.title}</p>
                <p className="text-sm text-muted-foreground mt-1">
                  Completed {formatDate(course.completedAt)}
                </p>
              </div>
            </div>
            <div className="flex gap-2 mt-4">
              {course.hasCertificate && (
                <Button variant="outline" size="sm" className="flex-1" asChild>
                  <Link href={`/moro-academy/certificates/${course.certificateId}`}>
                    <Award className="h-4 w-4 mr-2" />
                    View Certificate
                  </Link>
                </Button>
              )}
              <Button variant="ghost" size="sm" asChild>
                <Link href={`/moro-academy/courses/${course.id}`}>
                  Review
                </Link>
              </Button>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  </div>
</div>
```

---

## Certification Journey

### Certificate Display

```tsx
// Certificate View
<div className="container max-w-4xl py-12">
  {/* Certificate Card */}
  <Card className="overflow-hidden">
    {/* Certificate Design */}
    <div
      ref={certificateRef}
      className="aspect-[1.4/1] p-8 bg-gradient-to-br from-white to-blue-50 relative"
    >
      {/* Border Pattern */}
      <div className="absolute inset-4 border-2 border-primary/20 rounded-lg" />
      <div className="absolute inset-6 border border-primary/10 rounded-lg" />

      {/* Content */}
      <div className="relative h-full flex flex-col items-center justify-center text-center">
        {/* Logo */}
        <Image
          src="/images/moro-academy-logo.png"
          alt="MoroAcademy"
          width={120}
          height={40}
          className="mb-4"
        />

        <p className="text-sm text-muted-foreground uppercase tracking-wider">
          Certificate of Completion
        </p>

        <h1 className="text-2xl md:text-3xl font-bold mt-4 text-primary">
          {certificate.recipientName}
        </h1>

        <p className="text-muted-foreground mt-4 max-w-md">
          has successfully completed the course
        </p>

        <h2 className="text-xl font-semibold mt-2">
          {certificate.courseName}
        </h2>

        <p className="text-sm text-muted-foreground mt-4">
          Issued on {formatDate(certificate.issuedAt)}
        </p>

        {/* Signature */}
        <div className="mt-8 flex items-center gap-8">
          <div className="text-center">
            <div className="w-32 border-b border-muted-foreground" />
            <p className="text-sm mt-1">Course Instructor</p>
          </div>
          <div className="text-center">
            <div className="w-32 border-b border-muted-foreground" />
            <p className="text-sm mt-1">MoroAcademy Director</p>
          </div>
        </div>

        {/* Certificate ID */}
        <p className="absolute bottom-4 right-4 text-xs text-muted-foreground font-mono">
          ID: {certificate.id}
        </p>
      </div>
    </div>
  </Card>

  {/* Actions */}
  <div className="flex justify-center gap-4 mt-6">
    <Button onClick={downloadCertificate}>
      <Download className="h-4 w-4 mr-2" />
      Download PDF
    </Button>
    <Button variant="outline" onClick={shareCertificate}>
      <Share2 className="h-4 w-4 mr-2" />
      Share
    </Button>
    <Button variant="outline" asChild>
      <Link href={`/verify/${certificate.id}`} target="_blank">
        <ExternalLink className="h-4 w-4 mr-2" />
        Verify
      </Link>
    </Button>
  </div>

  {/* LinkedIn Share */}
  <Card className="mt-6">
    <CardContent className="p-4 flex items-center gap-4">
      <Linkedin className="h-8 w-8 text-[#0077B5]" />
      <div className="flex-1">
        <p className="font-medium">Add to LinkedIn</p>
        <p className="text-sm text-muted-foreground">
          Share your achievement with your professional network
        </p>
      </div>
      <Button variant="outline" onClick={addToLinkedIn}>
        Add to Profile
      </Button>
    </CardContent>
  </Card>
</div>
```

---

## Key UX Principles for Learning Platforms

### 1. Progress is Motivating
- Show clear progress indicators everywhere
- Celebrate milestones (25%, 50%, 75%, 100%)
- Streak tracking for daily learning

### 2. Mobile Learning is Essential
- Downloadable content for offline access
- Portrait-friendly video player
- Bite-sized lessons (<10 minutes)

### 3. Reduce Friction to Start
- No signup required to browse
- Quick enrollment (one click for free courses)
- Auto-resume from last position

### 4. Social Proof & Credentials
- Show enrollment numbers
- Display certificates prominently
- Enable certificate sharing

### 5. Support Different Learning Styles
- Video content with captions
- Downloadable resources
- Quizzes for self-assessment
- Note-taking features

---

## BARMM-Specific UX Design Implications (BDP 2023-2028)

Based on the Bangsamoro Development Plan 2023-2028 Chapter 9 data, MoroAcademy must address these design considerations:

### 1. Accessibility for Low Literacy Levels
- **Context**: 71.6% functional literacy rate (lowest in country)
- **Design Response**:
  - Heavy use of visual learning (icons, images, videos)
  - Simple, clear language (avoid jargon)
  - Audio narration for text content
  - Progress shown visually, not just numerically

### 2. Offline-First Design
- **Context**: Island provinces (BaSulTa) with limited connectivity
- **Design Response**:
  - Downloadable lessons for offline viewing
  - Low-bandwidth video options
  - Progress syncs when connection restored
  - SMS-based progress notifications as backup

### 3. Mobile-First Priority
- **Context**: Rural areas, limited access to computers
- **Design Response**:
  - Portrait-friendly video player
  - Thumb-friendly navigation
  - Minimal data consumption
  - Works on basic smartphones

### 4. Cultural Sensitivity
- **Context**: Madaris education integration, Islamic values
- **Design Response**:
  - Respect for prayer times in scheduling
  - Halal considerations in content
  - Option for gender-separated learning spaces (live workshops)
  - Arabic/local language support options

### 5. Trauma-Informed Design
- **Context**: 93,525 IDPs, conflict-affected communities
- **Design Response**:
  - Calm, non-stressful interface
  - No time pressure on assessments
  - Flexible pace of learning
  - Support resources easily accessible

### 6. TVET Integration
- **Context**: High demand for certification, limited assessment centers
- **Design Response**:
  - Clear certification pathways
  - Competency-based progress tracking
  - TESDA-aligned course structure
  - Virtual assessment preparation

### 7. Multi-Provider Support
- **Context**: CSEA, Coops, SEs, TSPs, development partners all provide training
- **Design Response**:
  - Provider branding options
  - Unified certificate format
  - Cross-provider course discovery
  - Provider analytics dashboards

### 8. Gender-Responsive Design
- **Context**: Women empowerment programs (WECoRe, Women Livelihood Acceleration)
- **Design Response**:
  - Women-focused course categories
  - Privacy options for women learners
  - Child-friendly scheduling considerations
  - Community learning group features

### 9. PWD Accessibility
- **Context**: 53,483 PWDs with capacity development needs
- **Design Response**:
  - WCAG 2.2 AA compliance
  - Screen reader compatibility
  - Keyboard navigation
  - Adjustable font sizes and contrast
  - Captions and transcripts for all video content

### 10. Integration with Social Protection Programs
- **Context**: 4Ps, SLP, Social Pension beneficiaries
- **Design Response**:
  - Beneficiary verification integration
  - Livelihood skills aligned with SLP requirements
  - Certificate recognition for program compliance
  - Referral pathways to government programs
